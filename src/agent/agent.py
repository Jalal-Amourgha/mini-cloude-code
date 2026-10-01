import json

class Agent:
    """Manage an AI agent that interacts with tools to complete user tasks.

    The agent maintains conversation history, sends messages to the language
    model, executes requested tool calls, and returns tool results to the
    model until a final response is generated or the iteration limit is
    reached.

    Attributes:
        client: The API client used to communicate with the language model.
        messages (list[dict]): The conversation history.
        functions_schemas (list[dict]): The schemas describing available tools.
        available_functions (dict): A mapping of tool names to Python functions.
        iterations (int): The maximum number of model iterations.
    """
    def __init__(
        self,
        client,
        system_prompt,
        functions_schemas=None,
        available_functions=[],
        iterations=20
    ):
        self.client = client
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]
        self.functions_schemas = functions_schemas or []
        self.available_functions = available_functions
        self.iterations = iterations

        self._execute()

    def _execute(self):
        user_prompt = input("Hi! How can I assist you today? ")

        if not user_prompt.strip():
            return

        self.messages.append({
            "role": "user",
            "content": user_prompt
        })

        for _ in range(self.iterations):
            try:
                response = self.client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=self.messages,
                    tools=self.functions_schemas or None,
                )

                message = response.choices[0].message
                tool_calls = message.tool_calls or []


                assistant_message = {
                    "role": "assistant",
                    "content": message.content,
                }

                if tool_calls:
                    assistant_message["tool_calls"] = [
                        call.model_dump(exclude_none=True)
                        for call in tool_calls
                    ]

                self.messages.append(assistant_message)


                if not tool_calls:
                    print(message.content or "")
                    return

                
                for tool in tool_calls:
                    func_name = tool.function.name

                    try:
                        function_args = json.loads(
                            tool.function.arguments or "{}"
                        )

                        if func_name not in self.available_functions:
                            result = {
                                "error": f"Unknown tool: {func_name}"
                            }
                        else:
                            result = self.available_functions[func_name](
                                **function_args
                            )

                    except Exception as e:
                        result = {"error": str(e)}

                    if isinstance(result, str):
                        tool_content = result

                    else:
                        tool_content = json.dumps(
                            result,
                            ensure_ascii=False,
                            default=str
                        )

                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool.id,
                        "content": tool_content,
                    })


            except Exception as e:
                print(f"Agent error: {e}")
                return

        print(
            f"Stopped: reached the maximum of "
            f"{self.iterations} model iterations."
        )