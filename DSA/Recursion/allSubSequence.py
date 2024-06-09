def subSequence(array):
    result = []
    output = []

    def solve(index, output):
        if index >= len(array):
            if output:
                result.append(output[:])
            return

        #inclusion case
        output.append(array[index])
        solve(index+1, output)

        #exclusion case
        output.pop()
        solve(index+1, output)

    solve(0, output)
    return result

print(subSequence([1,2,3,4,5,6,7 ]))

