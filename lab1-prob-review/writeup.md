# Prob Review Lab Write-up
## Marcel Pratikto


## Part 1

### Output of test_part1.py

```python
test/test_part1.py::TestFunctionEvaluatePMF::test_throws_when_probabilities_do_not_sum_to_one PASSED                                                                                                                    [  6%] 
test/test_part1.py::TestFunctionEvaluatePMF::test_throws_when_passed_negatively_likely_outcomes PASSED                                                                                                                  [ 13%] 
test/test_part1.py::TestFunctionEvaluatePMF::test_correct_for_two_dice_sum PASSED                                                                                                                                       [ 20%] 
test/test_part1.py::TestFunctionEvaluatePMF::test_correct_for_two_dice_diff PASSED                                                                                                                                      [ 26%] 
test/test_part1.py::TestFunctionEvaluatePMF::test_correct_for_rolling_doubles PASSED                                                                                                                                    [ 33%] 
test/test_part1.py::TestFunctionExpectedValue::test_throws_when_probabilities_do_not_sum_to_one PASSED                                                                                                                  [ 40%] 
test/test_part1.py::TestFunctionExpectedValue::test_throws_when_passed_negatively_likely_outcomes PASSED                                                                                                                [ 46%] 
test/test_part1.py::TestFunctionExpectedValue::test_throws_when_passed_empty_pmf PASSED                                                                                                                                 [ 53%] 
test/test_part1.py::TestFunctionExpectedValue::test_correct_for_two_dice_sum PASSED                                                                                                                                     [ 60%] 
test/test_part1.py::TestFunctionExpectedValue::test_correct_for_two_dice_diff PASSED                                                                                                                                    [ 66%] 
test/test_part1.py::TestFunctionVariance::test_throws_when_probabilities_do_not_sum_to_one PASSED                                                                                                                       [ 73%] 
test/test_part1.py::TestFunctionVariance::test_throws_when_passed_negatively_likely_outcomes PASSED                                                                                                                     [ 80%] 
test/test_part1.py::TestFunctionVariance::test_throws_when_passed_empty_pmf PASSED                                                                                                                                      [ 86%] 
test/test_part1.py::TestFunctionVariance::test_correct_for_two_dice_sum PASSED                                                                                                                                          [ 93%] 
test/test_part1.py::TestFunctionVariance::test_correct_for_two_dice_diff PASSED                                                                                                                                         [100%] 
```

### 1.4 Wrap Up
* Why does the PMF for the sum of two dice look the way it does? Can you explain why a value of 7 is more likely than a value of 10?
    * The PMF for the sum of two dice look the way it does because the likelihood of getting a number in the middle is higher than a low number or a high number. In the case of two six-sided dice, a value of 7 is more likely than a value of 10. The reason why is because there are more combinations of (1 to 6) + (1 to 6) that adds up to 7 than there are that adds up to 10.
        * 10: 4+6, 5+5
        * 7: 1+6, 2+5, 3+4

