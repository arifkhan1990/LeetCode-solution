class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            if i > 0:
                st.append(i)
            else:
                while st and st[-1] > 0 and st[-1] < abs(i):
                    st.pop()
                if not st or st[-1] < 0:
                    st.append(i)
                elif st[-1] + i == 0:
                    st.pop()
        return st