#!/usr/bin/env python3
import numpy as np

import ufal.chu_liu_edmonds

np.random.seed(43)
score_matrix = np.random.rand(3, 3)
heads, tree_score = ufal.chu_liu_edmonds.chu_liu_edmonds(score_matrix)
print(score_matrix)
print(heads, tree_score)
