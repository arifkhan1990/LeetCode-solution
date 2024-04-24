class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        for i in pushed:
            st.append(i)
            while st and popped and st[-1] == popped[0]:
                st.pop()
                popped.pop(0)
        while popped:
            if st[-1] != popped[0]:
                return 0
            popped.pop(0)
            st.pop()
        return 1