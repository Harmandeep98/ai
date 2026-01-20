import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo");

print(enc.encode("Hello, world!"));