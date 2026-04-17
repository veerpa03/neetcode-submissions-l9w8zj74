class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            i=0

            local = ""

            while i <len(email) and email[i]!= "+":
                if email[i] != ".":
                    local += email[i]
                i+=1

            domain = ""

            while i<len(email) and email[i]!="@":
                i+=1

            domain = email[i:]

            combine = local  + domain

            unique.add(combine)

        return len(unique)

