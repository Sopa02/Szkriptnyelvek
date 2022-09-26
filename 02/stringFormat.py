


def main():
    list1 = [1988,1990,2001,2004,2010]
    list2 = ['adat1','adat2','adat3','adat4','adat5']
    list3 = ['nem','nem','igen','nem','igen']

    print("{0:^10} {1:^12} {2:^12}".format('Sor1','Sor2','Sor3'))
    print('-'*35)
    for i in range(5):
        print("{0:^10} {1:^12} {2:^12}".format(list1[i],list2[i],list3[i]))






if __name__ == '__main__':
    main()
