# AlgorithmCoding

As part of the efforts to prepare for coding interviews, I practiced some problems in Python/C++ on leetcode as well as other CP websites like codeforces.
I list some of the interesting and/or challenging problems as follows.

## Combinatorial games
* [codeforces 1312F attack on red kingdom](https://codeforces.com/contest/1312/problem/F) \[[Solution](codeforces/1312F_attack_on_red_kingdom.cpp)\]: this problem touches upon the topic of combinatorial games. Refer to the [article](https://codeforces.com/blog/entry/66040) on codeforces or a Youtube [video](https://www.youtube.com/watch?v=ymoSFrDmkMY&list=PLOzRYVm0a65fY-Vh8Caiv3wAYmDd7SnrN&index=7)

## Dynamic programming
* [codeforces 1324F maximum white subtree](https://codeforces.com/contest/1324/problem/F)\[[Solution](codeforces/1324F_maximum_white_subtree.cpp)\]: dp on tree with a special technique called rerooting

* [Leetcode 730. Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/)\[[Solution](leetcode/730_count_different_palindromic_subsequences.py)\]: dp on the interval of a string

## Trees
* [codeforces 1328E tree queries](https://codeforces.com/contest/1328/problem/E)\[[Solution](codeforces/1328E_tree_queries.cpp)\]: application of lca. Learn a useful technique for lca, i.e., binary lifting, which is efficient for multiple lca queries.

## Two Pointers
* [Leetcode 1574 Shortest Subarray to be Removed to Make Array Sorted](https://leetcode.com/contest/biweekly-contest-34/problems/shortest-subarray-to-be-removed-to-make-array-sorted/)\[[Solution](leetcode/1574_shortest_subarray_to_be_removed_to_make_array_sorted.cpp)\]: interesting two pointer problem
* [Leetcode 1004 Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)\[[Solution](leetcode/1004_max_consecutive_ones_iii.cpp)\]: two pointer problem

## Greedy
* [Leetcode 1585 Check If String Is Transformable With Substring Sort Operations](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/)\[[Solution](leetcode/1585_check_if_string_is_transformable_with_substring_sort_operations.cpp
)\]: use the bubble sort idea

* [codeforces 1187D Subarray Sorting](https://codeforces.com/contest/1187/problem/D)\[[Solution](codeforces/1187D_subarray_sorting.cpp
)\]: use BIT to query/update the left boundary of each element


## Heap
* [Leetcode 1606. Find Servers That Handled Most Number of Requests](https://leetcode.com/contest/biweekly-contest-36/problems/find-servers-that-handled-most-number-of-requests/)\[[Solution](leetcode/1606_find_servers_that_handled_most_number_of_requests.cpp)\]: use ordered set to maintain the list of free servers and use priority queue to maintain the list of busy servers

## Recursion
* [Leetcode 1611. Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero//)\[[Solution](leetcode/1611_minimum_one_bit_operations_to_make_ingeters_zero.py)\]: find patterns of recursion. Another solution is to realize that this to find the order of the number in the gray code sequence
* [Leetcode 297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)\[[Solution](leetcode/297_serialize_and_deserialize_binary_tree.py)\]: besides bfs, pre-order traversal can also be used to serialize/deserialize binary tree in a recursive fashion. Be sure to know both approaches.

## Math
* [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)\[[Solution](leetcode/382_linked_list_random_node.py)\]: reservior sampling
