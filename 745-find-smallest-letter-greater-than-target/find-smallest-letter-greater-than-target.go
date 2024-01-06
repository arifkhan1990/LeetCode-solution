func nextGreatestLetter(letters []byte, target byte) byte {
    l, r, n := 0, len(letters), len(letters)
    
    for l < r {
        m := l + (r-l)/2
        
        if letters[m] <= target{
            l = m+1
        }else{
            r = m
        }
    }
    return letters[l%n]
}