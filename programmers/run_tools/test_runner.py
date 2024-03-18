def run_tests(test_function, expected_results, *args):
    for i, test_case in enumerate(args[0]):
        print(f"{i+1}번째 테스트 케이스")
        result = test_function(*[args[j][i] for j in range(len(args))])
        print(f"실행 결과: {result}")
        print("기대값: ", expected_results[i])
        print()
