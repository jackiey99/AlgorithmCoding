class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s):
            if len(s) > 4:
                return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if len(IP.split('.')) == 4 and all(isIPv4(s) for s in IP.split('.')):
            return "IPv4"
        if len(IP.split(':')) == 8 and all(isIPv6(s) for s in IP.split(':')):
            return "IPv6"
        return "Neither"


if __name__ == '__main__':
    s = Solution()
    ip = "2001:0db8:85a3:0:0:8A2E:B370:7334"
    print(s.validIPAddress(ip))
