while True:
    try:
        x = int(input("숫자입력 >>>"))
        result = 10 / x
    except ZeroDivisionError:
        print("어떤 수를 0으로 나누기 시도 오류")
        continue
    except ValueError:
        print("부적절한 값 오류")
        continue
    except TypeError:
        print("연산이나 함수에 이용되는 값의 자료형 오류")
        continue
    except IndexError:
        print("리스트나 문자열의 인덱스가 범위를 벗어난 오류")
        continue
    except KeyError:
        print("딕셔너리 인덱싱 연산자의 키가 존재하지 않을 때 오류")
        continue
    except NameError:
        print("존재하지 않는 함수나 변수 사용 오류")
        continue
    except FileNotFoundError:
        print("파일이나 폴더의 경로가 존재하지 않을 떄 오류")
        continue
    except ImportError:
        print("모듈을 가져오지 못했을 때 오류")
        continue
    except SyntaxError:
        print("코드에 문법 오류가 있을 때 오류")
        continue
    except:
        print("알수 없는 오류 발생")
        break
    
data = {"사과": 5, "바나나": 7}
try:
    print(data["오렌지"])
except KeyError:
    print("그 과일은 딕셔너리에 없습니다.") #. 오렌지는 딕셔너리 인덱싱 연산자의 키가 존재하지 않음
except:
    print("알수 없는 오류")

numbers = [1, 2, 3]
index = int(input("인덱스 입력"))
try: 
    print(numbers[index])
except IndexError:
    print("잘못된 인덱스")
except:
    print("예기치 않은 오류")