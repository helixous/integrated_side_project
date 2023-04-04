import datetime
from functools import wraps


def execution_time_checker(func):
    """
    함수의 수행시간을 체크하는 데코레이터.
    """

    # wraps(func)의 쓰임새를 제대로 이해하게 되었음.
    # wraps는 위에서 받은 함수를 인자로 그대로 넘겨준다
    @wraps(func)
    def decorator(*args, **kwargs):
        start = datetime.datetime.now()
        # 타겟함수의 수행결과를 funcResult에 저장해서 넘겨주어야 한다.
        func_result = func(*args, **kwargs)
        end = datetime.datetime.now()
        result = end - start
        print(f"{func.__name__}함수 수행시간:", result)
        # 타겟함수의 수행결과를 리턴하자.
        return func_result

    # 데코레이터함수의 수행결과를 리턴한다.
    return decorator
