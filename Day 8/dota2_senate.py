class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q, dire_q = [], []
        for i, s in enumerate(senate):
            if s == "R":
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while radiant_q and dire_q:
            radiant_idx, dire_idx = radiant_q.pop(0), dire_q.pop(0)
            if radiant_idx < dire_idx:
                radiant_q.append(radiant_idx + len(senate))
            else:
                dire_q.append(dire_idx + len(senate))

        return "Radiant" if radiant_q else "Dire"
