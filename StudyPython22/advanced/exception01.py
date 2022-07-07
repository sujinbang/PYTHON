# 예외처리 1 - 예외발생

# break point 'F9'/ step 실행 'F10'/ step into 'F11' / 디버깅 시작 'F5'

def multi(a, b):
    res = a * b
    return res

def divide(a, b):
    res = 0

    try:
        res = a / b
    except Exception as e:
        print(f'예외발생 {e}')
    finally:
        return res

    #if b == 0: return 0

    return res

if __name__ == '__main__':
    value = 7
    print('곱셈/나눗셈')
    print(multi(6,6))
    print('종료')