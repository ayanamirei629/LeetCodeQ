class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result=set()
        for email in emails:
            email_name,email_domain=email.split("@")
            if "+" in email_name:
                email_name=email_name[:email_name.index("+")].replace(".","")
            result.add(email_name+"@"+email_domain)
        return len(result)   

a = Solution()
emails =  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print a.numUniqueEmails(emails)
