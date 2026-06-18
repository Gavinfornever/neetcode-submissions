import ast
class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(strs)
    def decode(self, s: str) -> List[str]:
        return ast.literal_eval(s)