class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                top = matrix[l][l+i]
                matrix[l][l+i]=matrix[r-i][l]#topleft = bottom left
                
                matrix[r-i][l]=matrix[r][r-i]#bottomleft=bottomright

                matrix[r][r-i] = matrix[l+i][r] #bottomright = topright

                matrix[l+i][r]=top#topright=topleft
            l+=1
            r-=1

