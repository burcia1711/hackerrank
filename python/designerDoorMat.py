if __name__ == '__main__':
        R, C = map(int, input().split(" "))

        for i in range(R):
                pattern = ".|."
                if i < (R-1)/2:
                        print((pattern * (2*i+1)).center(C, "-"))
                elif i == (R-1)/2:
                        print("WELCOME".center(C, "-"))
                else:
                        print((pattern * (2*(R-1-i)+1)).center(C, "-"))