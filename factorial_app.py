import time

# 테스트 데이터
TEST = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]


# 1) 반복
def factorial_iter(n):
    if n < 0:
        raise ValueError("정수가 아닙니다.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 2) 재귀
def factorial_rec(n):
    if n < 0:
        raise ValueError("정수가 아닙니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


# 3) 실행 시간 측정 함수
def run_with_time(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    tresult = end - start
    return result, tresult


# 4) 정수 검사
def get_int(p="정수를 입력하세요: "):
    user = input(p)
    if not user.isdigit():
        raise ValueError("정수가 아닙니다.")
    return int(user)


# 5) 메뉴
def show_menu():
    print("\n======= Factorial Tester =======")
    print("1. 반복 방식으로 계산")
    print("2. 재귀 방식으로 계산")
    print("3. 두 방식 모두 계산 및 비교")
    print("4. 테스트 데이터 일괄 실행")
    print("q. 종료")
    print("================================")

# 6) 테스트
def test_cases():
    print("\n--- 테스트 데이터 실행 ---")
    for n in TEST:
        print(f"\n[n = {n}]")
        try:
            iter_result, iter_time = run_with_time(factorial_iter, n)
        except Exception as e:
            iter_result = f"에러: {e}"
            iter_time = None

        try:
            rec_result, rec_time = run_with_time(factorial_rec, n)
        except Exception as e:
            rec_result = f"에러: {e}"
            rec_time = None

        # 결과 비교
        if isinstance(iter_result, int) and isinstance(rec_result, int):
            match = iter_result == rec_result
        else:
            match = False

        print(f"결과 일치: {'일치' if match else '불일치'}")
        print(f"[반복] 실행 시간: {iter_time:.6f}초")
        print(f"[재귀] 실행 시간: {rec_time:.6f}초")
        print(f"{n}! = {iter_result}")

# 7) 메인 함수
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == 'q':
            print("프로그램을 종료합니다.")
            break

        elif choice in ['1', '2', '3']:
            try:
                n = get_int("n 값을 입력하세요: ")

            except ValueError as ve:
                print(f"[오류] {ve}")
                continue


            if choice == '1':
                try:
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    print(f"반복 방식 결과: {iter_result}")
                    print(f"실행 시간: {iter_time:.6f}초")
                except Exception as e:
                    print(f"[오류] {e}")

            elif choice == '2':
                try:
                    rec_result, rec_time = run_with_time(factorial_rec, n)
                    print(f"재귀 방식 결과: {rec_result}")
                    print(f"실행 시간: {rec_time:.6f}초")
                except Exception as e:
                    print(f"[오류] {e}")

            elif choice == '3':
                try:
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    rec_result, rec_time = run_with_time(factorial_rec, n)

                    print(f"[반복] 결과: {iter_result} | 시간: {iter_time:.6f}초")
                    print(f"[재귀] 결과: {rec_result} | 시간: {rec_time:.6f}초")

                    if isinstance(iter_result, int) and isinstance(rec_result, int):
                        match = iter_result == rec_result
                    else:
                        match = False

                    print(f"결과 일치 여부: {'일치' if match else '불일치'}")

                except Exception as e:
                    print(f"[오류] {e}")

        elif choice == '4':
            test_cases()

        else:
            print("유효하지 않은 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()