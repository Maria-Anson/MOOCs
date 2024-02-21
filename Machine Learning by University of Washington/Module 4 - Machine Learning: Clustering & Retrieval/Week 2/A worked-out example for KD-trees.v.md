# (OPTIONAL) A worked-out example for KD-trees
> 
> # A worked-out example for KD-trees
> 
> In applications where the number of features is not too high, KD-trees enable efficient queries for nearest neighbor search.
> 
> ## Dataset
> 
> Let us consider a toy example with six data points in 2D:
> 
> X
> 
> Y
> 
> Data point 0
> 
> 0.59
> 
> 0.9
> 
> Data point 1
> 
> 0.89
> 
> 0.82
> 
> Data point 2
> 
> 0.04
> 
> 0.69
> 
> Data point 3
> 
> 0.38
> 
> 0.52
> 
> Data point 4
> 
> 0.66
> 
> 0.19
> 
> Data point 5
> 
> 0.27
> 
> 0.72
> 
> Data point 6
> 
> 0.8
> 
> 0.6
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/zz4MR3PfEead-BJkoDOYOw_9fa8ad94d4ecdea8e47d0b1e3d8847e1_download.png?expiry=1656979200000&hmac=l0mJ7N_revbYf9tLQiGPy1V7Qii_asGULKdOKuuN_iY)
> 
> ## KD-tree construction: first split
> 
> Let’s split data into two groups. We do so by comparing the X coordinate of each data point against 0.465\. (We’ll soon get back to how we got to choose this point of reference, in the next section.)
> 
> X
> 
> Y
> 
> **X vs 0.465 ?**
> 
> Data point 0
> 
> 0.59
> 
> 0.9
> 
> **>= 0.465**
> 
> Data point 1
> 
> 0.89
> 
> 0.82
> 
> **>= 0.465**
> 
> Data point 2
> 
> 0.04
> 
> 0.69
> 
> **< 0.465**
> 
> Data point 3
> 
> 0.38
> 
> 0.52
> 
> **< 0.465**
> 
> Data point 4
> 
> 0.66
> 
> 0.19
> 
> **>= 0.465**
> 
> Data point 5
> 
> 0.27
> 
> 0.72
> 
> **< 0.465**
> 
> Data point 6
> 
> 0.8
> 
> 0.6
> 
> **>= 0.465**
> 
> The data points whose X coordinate is less than 0.465 are grouped together in one node; the remaining data points are grouped together in another.
> 
> **Node 0**
> 
> X
> 
> Y
> 
> Data point 2
> 
> 0.04
> 
> 0.69
> 
> Data point 3
> 
> 0.38
> 
> 0.52
> 
> Data point 5
> 
> 0.27
> 
> 0.72
> 
> **Node 1**
> 
> X
> 
> Y
> 
> Data point 0
> 
> 0.59
> 
> 0.9
> 
> Data point 1
> 
> 0.89
> 
> 0.82
> 
> Data point 4
> 
> 0.66
> 
> 0.19
> 
> Data point 6
> 
> 0.8
> 
> 0.6
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/NCAoqXPgEealOA67wFuqoQ_73fae8f70cdecbd78333318b4b3f6886_download-_1_.png?expiry=1656979200000&hmac=LlGI2J6tmga1s34ewdL42LAZnPh5bjn6AshRaO455FE)
> 
> At each node, we keep one additional piece of information: the tight coordinate bounds of the points inside the node. This information will be useful in performing nearest neighbor search.
> 
> **Tight bounds**
> 
> X
> 
> Y
> 
> **Node 0**
> 
> **0.04 <= X <= 0.38**
> 
> **0.52 <= Y <= 0.72**
> 
> **Node 1**
> 
> **0.59 <= X <= 0.89**
> 
> **0.19 <= Y <= 0.9**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/hExzqXPgEeazqQoyai5dlw_5c65f0dbcc3880bb8aacf08301fd0ae5_download-_2_.png?expiry=1656979200000&hmac=Z8mery2xLNcTzaPR3Kb6BoDFjthQF6p1FKiXZc3jOKs)
> 
> We encode the hierarchy among the nodes as a binary tree:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/wcwpsnPgEeamDApmnD43Fw_54347f50247cc0ed7f3b8132d1e7caf4_Screenshot-from-2016-09-05-17-10-29.png?expiry=1656979200000&hmac=MjhKIH0x3uzJ1caHcH4Fib065MNlW4fMTq3Hb4X2Te4)
> 
> ## KD-tree construction: recursive split
> 
> After the first split, we further subdivide each node in recursive fashion. There are some decisions we have to make each time we split a node. **Note that there are many possible heuristics when it comes to splitting decisions; we choose a particular set for the sake of illustration.**
> 
> *   **Which dimension (axis) do we split along?** For this example, **we alternate between the X axis and the Y axis.** This is why the first split used the X coordinates.
> 
> *   **Which value do we split at? Let’s split at the midpoint between the smallest and largest coordinates among the member points.** In the first split, for instance, we took the midpoint in the smallest and largest X coordinates, giving 0.465\. Notice we say “member points”: when it comes to subsequent splits, we consider only those points that are inside the node being split. (Note: some heuristics may use dimensions of the box instead of the member points.)
> 
> *   **When do we stop? Let’s stop when the node contains two nodes.**
> 
> With this set of heuristics, let’s first subdivide Node 0\. The node will be divided into two nodes, Nodes 2 and 3, as follows:
> 
> *   Since the first split used the X axis, use the Y axis.
> 
> *   Take the midpoint of the Y coordinates of the member points, i.e. data points 2, 3, and 5\. The midpoint is (0.52+0.72)/2 = 0.62.
> 
> *   The points whose Y coordinate is less than 0.62 go into Node 2; the others go into Node 3.
> 
> *   Compute the tight bounds for Nodes 2 and 3.
> 
> **Node 0**
> 
> X
> 
> **Y**
> 
> **Y vs 0.62 ?**
> 
> **Which node?**
> 
> Data point 2
> 
> 0.04
> 
> **0.69**
> 
> **>= 0.62**
> 
> **To Node 3**
> 
> Data point 3
> 
> 0.38
> 
> **0.52**
> 
> **< 0.62**
> 
> **To Node 2**
> 
> Data point 5
> 
> 0.27
> 
> **0.72**
> 
> **>= 0.62**
> 
> **To Node 3**
> 
> **Tight bounds**
> 
> X
> 
> Y
> 
> Node 0
> 
> 0.04 <= X <= 0.38
> 
> 0.52 <= Y <= 0.72
> 
> Node 1
> 
> 0.59 <= X <= 0.89
> 
> 0.19 <= Y <= 0.9
> 
> **Node 2**
> 
> **0.38 <= X <= 0.38**
> 
> **0.52 <= Y <= 0.52**
> 
> **Node 3**
> 
> **0.04 <= X <= 0.27**
> 
> **0.69 <= Y <= 0.72**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/aqhaj3PiEeamDApmnD43Fw_9e787ee87f47c96689ae882cb1440a40_download-_3_.png?expiry=1656979200000&hmac=yUNuslw-4Z7VTJuryxf9hQiUJYqihfIx0f0cW43vbsc)
> 
> Note that Nodes 2 and 3 have much smaller boxes than Node 0\. Tighter bounds would help speed up nearest neighbor search. The hierarchy has now two levels, with a new subtree added to the left:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/d4Dt6nPiEealOA67wFuqoQ_36ffa3175fb4b0988b9611f6925599be_Screenshot-from-2016-09-05-17-12-54.png?expiry=1656979200000&hmac=XWdA9l3vtPk8Jmx_qExXEvLkJkuwn1lW13upuegu2Oo)
> 
> It only remains to split Node 1, as Nodes 2 and 3 have fewer than 2 points each. Node 1 will be divided into two nodes, Nodes 4 and 5, as follows:
> 
> *   Since the first split used the X axis, use the Y axis.
> 
> *   Take the midpoint of the Y coordinates of the member points, i.e. data points 0, 1, 4, and 6\. The midpoint is (0.19+0.9)/2 = 0.545.
> 
> *   The points whose Y coordinate is less than 0.545 go into Node 4; the others go into Node 5.
> 
> *   Compute the tight bounds for Nodes 4 and 5.
> 
> **Node 1**
> 
> X
> 
> **Y**
> 
> **Y vs 0.545 ?**
> 
> **Which node?**
> 
> Data point 0
> 
> 0.59
> 
> **0.9**
> 
> **>= 0.545**
> 
> **To Node 5**
> 
> Data point 1
> 
> 0.89
> 
> **0.82**
> 
> **>= 0.545**
> 
> **To Node 5**
> 
> Data point 4
> 
> 0.66
> 
> **0.19**
> 
> **< 0.545**
> 
> **To Node 4**
> 
> Data point 6
> 
> 0.8
> 
> **0.6**
> 
> **>= 0.545**
> 
> **To Node 5**
> 
> **Tight bounds**
> 
> X
> 
> Y
> 
> Node 0
> 
> 0.04 <= X <= 0.38
> 
> 0.52 <= Y <= 0.72
> 
> Node 1
> 
> 0.59 <= X <= 0.89
> 
> 0.19 <= Y <= 0.9
> 
> Node 2
> 
> 0.38 <= X <= 0.38
> 
> 0.52 <= Y <= 0.52
> 
> Node 3
> 
> 0.04 <= X <= 0.27
> 
> 0.69 <= Y <= 0.72
> 
> **Node 4**
> 
> **0.66 <= X <= 0.66**
> 
> **0.19 <= Y <= 0.19**
> 
> **Node 5**
> 
> **0.59 <= X <= 0.89**
> 
> **0.6 <= Y <= 0.9**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/tC0K5HPjEeaQkhKk4jYr6Q_aed15b4c544d78cab7a64df01e390e31_download-_4_.png?expiry=1656979200000&hmac=ck0-M2iSxK0cDOlTe-DgOdjzquJr0O6YUMwc2trbd8E)
> 
> The node hierarchy gets a new subtree added to the right:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/1qrZQHPjEeaTyQp_BD0w6w_0c03567b6660e318d9cb2bec707b11fb_Screenshot-from-2016-09-05-17-16-41.png?expiry=1656979200000&hmac=FxiTcp90jfqU8_2oN67M13AaLNUwRHSYg_yONyJroY4)
> 
> Finally, we split Node 5, as it’s still got 3 data points.
> 
> *   Since we used the Y axis for the previous split, let’s use the X axis this time.
> 
> *   Take the midpoint of the X coordinates of the member points, i.e. data points 0, 1, and 6\. The midpoint is (0.59+0.89)/2 = 0.74.
> 
> *   The points whose Y coordinate is less than 0.74 go into Node 6; the others go into Node 7.
> 
> *   Compute the tight bounds for Nodes 6 and 7.
> 
> **Node 5**
> 
> **X**
> 
> Y
> 
> **X vs 0.74 ?**
> 
> **Which node?**
> 
> Data point 0
> 
> **0.59**
> 
> 0.9
> 
> **< 0.74**
> 
> **To Node 6**
> 
> Data point 1
> 
> **0.89**
> 
> 0.82
> 
> **>= 0.74**
> 
> **To Node 7**
> 
> Data point 6
> 
> **0.8**
> 
> 0.6
> 
> **>= 0.74**
> 
> **To Node 7**
> 
> **Tight bounds**
> 
> X
> 
> Y
> 
> Node 0
> 
> 0.04 <= X <= 0.38
> 
> 0.52 <= Y <= 0.72
> 
> Node 1
> 
> 0.59 <= X <= 0.89
> 
> 0.19 <= Y <= 0.9
> 
> Node 2
> 
> 0.38 <= X <= 0.38
> 
> 0.52 <= Y <= 0.52
> 
> Node 3
> 
> 0.04 <= X <= 0.27
> 
> 0.69 <= Y <= 0.72
> 
> Node 4
> 
> 0.66 <= X <= 0.66
> 
> 0.19 <= Y <= 0.19
> 
> Node 5
> 
> 0.59 <= X <= 0.89
> 
> 0.6 <= Y <= 0.9
> 
> **Node 6**
> 
> **0.59 <= X <= 0.59**
> 
> **0.9 <= Y <= 0.9**
> 
> **Node 7**
> 
> **0.8 <= X <= 0.89**
> 
> **0.6 <= Y <= 0.82**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/rfbQ6XPkEeazqQoyai5dlw_b0cceaae24dc8aa5364737e1d3ff3967_download-_5_.png?expiry=1656979200000&hmac=O6CkHksoT01BNprbda3hkek_cmOw-8gZ3wwThuygbD8)
> 
> The hierarchy of nodes has now three levels, with a new subtree in the very right:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/vQnqX3PkEealOA67wFuqoQ_2f3e976e1785a29a2d821017d7832ff6_Screenshot-from-2016-09-05-17-22-19.png?expiry=1656979200000&hmac=80ZdYIxjxVWP-qYCaDCfVt_9bThhbnhaRJO0-jnO6ms)
> 
> Now that each node contains at most two data points, we’re done.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0yeIzXPkEeaQkhKk4jYr6Q_2c9729728bca851982e987d8f3836307_download-_6_.png?expiry=1656979200000&hmac=8obJk3cur73V7Cige-ei9g1V5oFYKY3z1qU5M5LXlcY)
> 
> ## Querying the KD-tree
> 
> Suppose we’d like to find the nearest neighbor of the **query point (0.5, 0.66)**.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/_3FGUnPkEealOA67wFuqoQ_238f9d44ce3462946a840df7ee44f6a2_download-_7_.png?expiry=1656979200000&hmac=V92-Je9ojMpH3SEHTBrUxOCGVXA9UrGTCO78lUulAwU)
> 
> By visual inspection, we see that the query point falls inside Node 6\. Alternatively, we can locate the query point by **traversing down** the hierarchy of nodes.
> 
> *   X < 0.465 ? If Yes, go to Node 0; otherwise, go to Node 1 => **0.5 >= 0.465, so go to Node 1.**
> 
> *   Y < 0.545 ? If Yes, go to Node 4; otherwise, go to Node 5 => **0.66 >= 0.545, so go to Node 5**.
> 
> *   X < 0.74 ? If Yes, go to Node 6; otherwise, go to Node 7 => **0.5 < 0.74, so go to Node 6.**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/EfIPmnPlEeaTyQp_BD0w6w_387a7ac9d105b37abf1b2fa109cd0d64_Screenshot-from-2016-09-05-17-27-44.png?expiry=1656979200000&hmac=oi3G3vMROmdilekqV10kFvhGXLRdu8neGaUmBTPBfBM)
> 
> Once the query point is located in a **leaf node** (i.e. bottom-most), we perform **backtracking**: starting from the leaf node, we traverse up, updating our current guess for the nearest neighbor as we go.
> 
> Let’s start with the leaf node, Node 6\. It contains one data point, namely data point 0.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/LTZY3nPlEeazqQoyai5dlw_093f7d05c7c367204d314d3323cf369e_download-_9_.png?expiry=1656979200000&hmac=YJJPgi__O1WCg0N1FYS8NsEne0QaUielJAvwH1yR0zM)![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/NbtwD3PlEeam4BLcQYZr8Q_fa8b57d80204736fd59a7bfe3c9be076_Screenshot-from-2016-09-05-17-53-07.png?expiry=1656979200000&hmac=UfQSvX57-5v87NGoWbWv3Vf7geClPIdEuD8suZG2gRU)
> 
> The Euclidean distance between the query point and data point 0 is approximately 0.25632\. By definition, the nearest neighbor of the query must be closer to it than any other point. **So the nearest neighbor must be within distance 0.25632 of the query point. This observation will be crucial in performing an efficient nearest neighbor search.**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Rb-OInPnEeaNlA6zo4Pi2Q_ea0cbc2c282d64046a5c5a42c89e880a_download-_8_.png?expiry=1656979200000&hmac=R7Ytw91BCWy54dvUVxcRzUexDihiNOLS8FRPVGZmAPM)
> 
> We now traverse one level up, to Node 5\. **We do this because the nearest neighbor may not necessarily fall into the same node as the query point. Data point 0 is only the current estimate of the nearest neighbor; it may not be the true nearest neighbor.**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/VifXpHPnEeamDApmnD43Fw_ef760cc1c0738c2b4217275a56cc5f16_download-_10_.png?expiry=1656979200000&hmac=G1EfhKpfV_oXqovmy_dFIEmkRJZyFw0ebvDW_4m1Gds)![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/YWHVh3PnEead-BJkoDOYOw_cd81012521a2ea1ea9f8ef35b0503533_Screenshot-from-2016-09-05-18-18-14.png?expiry=1656979200000&hmac=2IwIBJIBqthPZT1ZaJMO95JMQp0_KJMl-fLeFtBH5zA)
> 
> Do we need to inspect all data points in Node 5? It turns out we don’t. **We look at the tight bounds of Node 7 to decide if we need to take a further look.** (If Node 5 contained the nearest neighbor but Node 6 did not, then by the process of elimination, Node 7 would contain the nearest neighbor.)
> 
> The bounds for Node 7 are 0.8 <= X <= 0.89 and 0.6 <= Y <= 0.82 for the X and Y axes respectively. By geometric argument, no point inside this box could fall inside the 0.25632 radius. That is, all points inside this box are farther from the query than data point 0\. **In general, we do two things:**
> 
> *   **Draw a circle around the query point so that it touches the current estimate of the nearest neighbor (data point 0).**
> 
> *   **See if the bounds for each nearby node has any overlap with the circle. If so, the estimate must be updated. Otherwise, the current estimate remains unmodified.**
> 
> In the case of Node 7, there is no overlap with the circle, so the node is **pruned away from the search.**
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/gtYiknPnEeaQkhKk4jYr6Q_b5c3885991e060793c12dbff895993eb_download-_11_.png?expiry=1656979200000&hmac=asRF7gTjh4_ul1dZ67A-CVQI7WWr66cg2-vK4ZHF68Y)
> 
> Let’s traverse up another level:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/lovp9HPnEeam4BLcQYZr8Q_34be13d3f9a4291214d4e2f5885b70fb_download-_12_.png?expiry=1656979200000&hmac=hK93frGZm6Tei-8ddfLDOkTtVcMYmS7ygw8kBrLz9DA)![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/oV07OXPnEealOA67wFuqoQ_7acbba8c0336a19583eaf738256b7ddc_Screenshot-from-2016-09-05-18-20-16.png?expiry=1656979200000&hmac=y7BqAJ9lohl7_yAGzbf7d0_nfq3SpE9nZ9pBiiJMfwY)
> 
> We inspect a nearby node, Node 4, for nearest neighbor search. Node 4 contains only a single point, and that point is far away from the circle. So Node 4 is pruned away as well.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/q5RukXPnEeaxYA6oVw19Xw_95567a0edf530ce8d0b97cea4f4ca76f_download-_13_.png?expiry=1656979200000&hmac=fdAX8O2xa_laIdWz2svvZqIe5OdD2i5sZctC6UlfMTs)
> 
> We traverse up one last time to reach the root node.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/uIrp03PnEeaxYA6oVw19Xw_a38be92a897ea61dc52b002d3911cc75_download-_14_.png?expiry=1656979200000&hmac=slDK0Td035v-EGcNeexRtB2YnUFbYYMa5J1sGIYufuw)![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/wNOUtXPnEeaQkhKk4jYr6Q_354e497918d7d297bf8c998f8952d2b9_Screenshot-from-2016-09-05-18-27-05.png?expiry=1656979200000&hmac=vih-POlmHRROnBnKZpQX7BqkpBc-Mt4-Kw1fGDqaqYI)
> 
> This time, the bounding box for Node 0 overlaps with the circle, indicating that Node 0 may contain a point that’s closer to the query than data point 0 is.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/02F9R3PnEeaQkhKk4jYr6Q_8597bf4eb02b0acc7ad6d77b0d196cda_download-_15_.png?expiry=1656979200000&hmac=IUYNIcDsPHkrItVxPFi0hCLPD_cT68c_s15cqlM_mAY)
> 
> To revise our estimate of the nearest neighbor, we inspect the child nodes of Node 0.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/3YvgAnPnEeazqQoyai5dlw_6778890dde4bd00164b454fdcfec0512_Screenshot-from-2016-09-05-19-14-40.png?expiry=1656979200000&hmac=6dYKxI6XY4l9pJrF8qA00zXKA17sfXnpYL4BDSF6dvg)
> 
> The bounding box for Node 2 has a slight overlap with the circle, and the sole data point in Node 3 is inside the circle as well. Therefore, we **f****ail to prune** Nodes 2 and 3\. Since both are leaf nodes, we have to inspect all data points in these nodes.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/9dM9KHPnEeaNlA6zo4Pi2Q_c4eedad5d7778c17042c49e318d61aab_download-_16_.png?expiry=1656979200000&hmac=7_vQJrv1slJLIvnPG37GmF8xpoxg6bEiIfoEbH-oQig)
> 
> We compare data points 0, 2, 3, and 5 using their distances from the query, and data point 3 comes out to be the closest:
> 
> Distance from the query (0.5, 0.66)
> 
> Data point 0 (0.59, 0.9)
> 
> 0.25632
> 
> Data point 2 (0.04, 0.69)
> 
> 0.46098
> 
> **Data point 3 (0.38, 0.52)**
> 
> **0.18439**
> 
> Data point 5 (0.27, 0.72)
> 
> 0.23770
> 
> The nearest neighbor estimate is now revised to be (0.38, 0.52):
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/IViYRnPoEeaxYA6oVw19Xw_2508393b81a383878d0bd09f54bc0d21_download-_18_.png?expiry=1656979200000&hmac=KthgOrt_8RbUCxLyJtprKbV0_Pp0VzuBlwtgLvkPL5s)
> 
> **Since we’ve reached the root node, we are done: data point 3 is indeed the true nearest neighbor of the query. Notice again how we could prune away two nodes from the nearest neighbor search just by using bounding boxes.**
> 
> **Note.** This reading used two-dimensional data for simplicity, but the process can be generalized to 3 dimensions or higher, by replacing "circles" with hyper-spheres and "rectangles" with hyper-rectangles.
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/uJh72/optional-a-worked-out-example-for-kd-trees#main
