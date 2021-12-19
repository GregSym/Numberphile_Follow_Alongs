# Numberphile_Follow_Alongs

![test_suite](https://github.com/GregSym/Numberphile_Follow_Alongs/actions/workflows/test-suite.yml/badge.svg)

Occassionally, Numberphile videos invite viewers to try some algorithmic challenges out for themselves, I'm placing some of my responses here

## Witness Numbers or the Miller Rabin Test

The challenge presented in the video is to take the following algorithm:

```
Input #1: n > 3, an odd integer to be tested for primality
Input #2: k, the number of rounds of testing to perform
Output: “composite” if n is found to be composite, “probably prime” otherwise

write n as 2^r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
WitnessLoop: repeat k times:
    pick a random integer a in the range [2, n − 2]
    x ← a^d mod n
    if x = 1 or x = n − 1 then
        continue WitnessLoop
    repeat r − 1 times:
        x ← x^2 mod n
        if x = n − 1 then
            continue WitnessLoop
    return “composite”
return “probably prime”
```

and find the values of a for which the test produces the most false positives. The solution implemented in the notebook is a simple brute force solution that runs to whatever number your RAM and time will allow it to run to.

## Hitomezashi Stitch Patterns

https://www.youtube.com/watch?v=JbfhzlMk2eY
<p>
description: Ayliean MacDonald discusses Hitomezashi Stitch Patterns.
</p>

A pattern generated from a 2d binary structure.

In the video it is declared a '2 colourable pattern', for which the included notebook implements an incredibly naive proof.
