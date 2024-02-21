## Decision Trees in Practice
> 
> Total points 14
> 
> ### 1.
> 
> Question 1
> 
> Given an intermediate node with 6 safe loans and 3 risky loans, if the min_node_size parameter is 10, what should the tree learning algorithm do next?
> 
> 1 point
> 

      Create a leaf and return it 
> 
>  Continue building the tree by finding the best splitting feature 
> 
> ### 2.
> 
> Question 2
> 
> Assume an intermediate node has 6 safe loans and 3 risky loans. For each of 4 possible features to split on, the error reduction is 0.0, 0.05, 0.1, and 0.14, respectively. If the minimum gain in error reduction parameter is set to 0.2, what should the tree learning algorithm do next?
> 
> 1 point
> 

      Create a leaf and return it 
> 
>  Continue building the tree by using the splitting feature that gives 0.14 error reduction 
> 
> ### 3.
> 
> Question 3
> 
> Consider the prediction path **validation_set[0]** with my_decision_tree_old and my_decision_tree_new. For my_decision_tree_new trained with
> 
>  `1
> 
> max_depth = 6, min_node_size = 100, min_error_reduction=0.0
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_1 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_1.drop-target, .monaco-list.list_id_1 .monaco-list-rows.drop-target, .monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> is the prediction path shorter, longer, or the same as the prediction path using my_decision_tree_old that ignored the early stopping conditions 2 and 3?
> 
> 1 point
> 

      Shorter 
> 
>  Longer 
> 
>  The same 
> 
> ### 4.
> 
> Question 4
> 
> Consider the prediction path for **ANY** new data point. For my_decision_tree_new trained with
> 
>  `1
> 
> max_depth = 6, min_node_size = 100, min_error_reduction=0.0
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_2:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_2 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_2 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_2:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_2.drop-target, .monaco-list.list_id_2 .monaco-list-rows.drop-target, .monaco-list.list_id_2 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> is the prediction path for a data point always shorter, always longer, always the same, shorter or the same, or longer or the same as for my_decision_tree_old that ignored the early stopping conditions 2 and 3?
> 
> 1 point
> 
>  **Always** shorter 
> 
>  **Always** longer 
> 
>  **Always** the same 
> 

      Shorter or the same 
> 
>  Longer or the same 
> 
> ### 5.
> 
> Question 5
> 
> For a tree trained on any dataset using parameters
> 
>  `1
> 
> max_depth = 6, min_node_size = 100, min_error_reduction=0.0
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> what is the maximum possible number of splits encountered while making a single prediction?
> 
> 1 point
> 

     6
> 
> ### 6.
> 
> Question 6
> 
> Is the validation error of the new decision tree (using early stopping conditions 2 and 3) lower than, higher than, or the same as that of the old decision tree from the previous assigment?
> 
> 1 point
> 
>  Higher than 
> 

      Lower than 
> 
>  The same 
> 
> ### 7.
> 
> Question 7
> 
> Which tree has the smallest error on the validation data?
> 
> 1 point
> 
>  model_1 
> 
>  model_2 
> 

      model_3 
> 
> ### 8.
> 
> Question 8
> 
> Does the tree with the smallest error in the training data also have the smallest error in the validation data?
> 
> 1 point
> 

      Yes 
> 
>   No 
> 
> ### 9.
> 
> Question 9
> 
> Is it always true that the tree with the lowest classification error on the training set will result in the lowest classification error in the validation set?
> 
> 1 point
> 
>  Yes, this is ALWAYS true. 
> 

      No, this is NOT ALWAYS true. 
> 
> ### 10.
> 
> Question 10
> 
> Which tree has the largest complexity?
> 
> 1 point
> 
>  model_1 
> 
>  model_2 
> 

      model_3 
> 
> ### 11.
> 
> Question 11
> 
> Is it always true that the most complex tree will result in the lowest classification error in the validation_set?
> 
> 1 point
> 
>  Yes, this is always true. 
> 

      No, this is not always true. 
> 
> ### 12.
> 
> Question 12
> 
> Using the complexity definition, which model (model_4, model_5, or model_6) has the largest complexity?
> 
> 1 point
> 

      model_4 
> 
>  model_5 
> 
>  model_6 
> 
> ### 13.
> 
> Question 13
> 
> model_4 and model_5 have similar classification error on the validation set but model_5 has lower complexity. Should you pick model_5 over model_4?
> 
> 1 point
> 

      Pick model_5 over model_4 
> 
>  Pick model_4 over model_5 
> 
> ### 14.
> 
> Question 14
> 
> Using the results obtained in this section, which model (model_7, model_8, or model_9) would you choose to use?
> 
> 1 point
> 
>  model_7 
> 

      model_8 
> 
>  model_9
>
> -- https://www.coursera.org/learn/ml-classification/exam/xRbhG/decision-trees-in-practice/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
