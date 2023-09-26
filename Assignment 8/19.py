original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'
elements1 = list(filter(lambda x: substring1 in x, original_list))
elements2 = list(filter(lambda x: substring2 in x, original_list))
print("Elements of the said list that contain specific substring:", elements1)
print("Elements of the said list that contain specific substring:", elements2)