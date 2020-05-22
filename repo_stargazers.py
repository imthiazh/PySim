def stargazer_comparison():
	import time

	res=time.ctime(12345678.99876)
	res1=time.ctime(13385678.87912)
	res2=time.ctime(19365678.65409)
	res3=time.ctime(200345678.12345)
	res4=time.ctime(13385678.87912)
	res5=time.ctime(123447678.99876)
	res6=time.ctime(99945678.99876)
	res7=time.ctime(88885678.87912)
	res8=time.ctime(99945678.99876)
	res9=time.ctime(90845678.99876)


	arr1=[["user1",res],["user2",res1],["user3",res2],["user4",res3],["user5",res4],["user6",res5],["user7",res6],["user8",res7],["user9",res8],["user10",res9],["user11",88111.222],["user12",31111.222],["user13",17711.222],["user14",11111.222],["user15",11122.222]]

	arr2=[["user20",13456.998],["user1",res],["user13",21432.222],["user12",21332.222],["user11",12489.222],["user21",res1],["user17",res2],["user18",res3],["user19",res4],["user10",res5],["user17",res6],["user30",res7],["user29",res8],["user14",res9],["user15",32145.123]]
	print("----- Repopal Stargazer Analysis -----")
	print()
	print("Report:")
	for i in range(len(arr1)):
		for j in range(len(arr2)):
			if arr1[i][1]==arr2[j][1] and arr1[i][0]==arr2[j][0] and i!=j:
				print(arr1[i][0]+ " had starred both the projects at " +arr1[i][1])
