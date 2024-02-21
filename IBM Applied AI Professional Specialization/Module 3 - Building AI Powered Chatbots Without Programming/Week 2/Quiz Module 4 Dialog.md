## Module 4 Quiz: Dialog
> 
> Latest Submission Grade
> 
> 100%
> 
> 1.
> 
> Question 1
> 
> Multiple conditional responses allow us to attach conditions to responses within a node.
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Check
> 
> Correct
> 
> That's right. They are quite handy.
> 
> 2.
> 
> Question 2
> 
> The order of nodes in the dialog can affect how the chatbot works.
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Check
> 
> Correct
> 
> For example, the order of the Welcome and Anything else node matters. Some nodes can be independent peers and appear anywhere between Welcome and Anything else. In other cases, however, the order of these middle nodes can matter as well. For example, nodes with generic conditions (e.g., @relationship) placed above nodes with related, but more specific conditions (e.g., @relationship:wife) can overshadow and prevent the execution of the latter.
> 
> 3.
> 
> Question 3
> 
> Node A has @occasion as its condition. Node B, placed just below node A, has @occasion:Graduation as its condition. Which of the following statements is true?
> 
> 1 / 1 point
> 
>  The order of node A and node B doesn't matter. 
> 
>  Both node A and node B will never be executed. 
> 
>  Node A is overshadowed and will not be executed (unless we explicitly jump to it). 
> 

      Node B is overshadowed and will not be executed (unless we explictily jump to it). 
> 
> Check
> 
> Correct
> 
> That's right. Since the user input could match both the @occasion entity condition and @occasion:Graduation entity value condition, Node A placed above node B will always be executed instead. Node B will not be executed unless we jump to it from Node A or somewhere else in the dialog.
> 
> 4.
> 
> Question 4
> 
> In general, child nodes are considered if the parent node condition is met.
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Check
> 
> Correct
> 
> Yes.
> 
> 5.
> 
> Question 5
> 
> Select all the statements that are true.
> 
> 3 / 3 points
> 
>  Chatbot prompts should be as generic as possible (e.g., Hello. Ask me anything.) 
> 

      We should avoid "yes" and "no" answers when possible 
> 
> Check
> 
> Correct
> 
> This can lead to answers that are factually wrong if the user phrases the question differently.
> 
>  Very long responses are good 
> 

      When designing a chatbot, we should consider tone and personality. 
> 
> Check
> 
> Correct
> 
> Absolutely.
> 

      The tone and personality of our chatbot can affect how well it is perceived by the user. 
> 
> Check
> 
> Correct
> 
> Indeed.
>
> -- https://www.coursera.org/learn/building-ai-powered-chatbots/exam/oYKOp/module-4-quiz-dialog/attempt?redirectToCover=true#Tunnel Vision Close
