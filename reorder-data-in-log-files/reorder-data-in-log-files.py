class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter=[]
        digit=[]
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else :
                letter.append(log)
        letter.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return letter+digit
        