while True:
    print("\n1. 인사하기")
    print("2. 안녕히가세요")
    print("3. 종료하기")
    
    a = input("원하는 메뉴의 번호를 입력하세요: ")
    
    if a == '1':
        print("안녕하세요!")
    elif a == '2':
        print("안녕히가세요!")
    elif a == '3':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")

