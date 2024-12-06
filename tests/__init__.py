"""
Python에서 디렉토리를 패키지로 인식시키기 위해 필요한 것으로
패키지 인식을 위해서는 해당 디렉토리에 __init__.py 파일이 있어야 한다.
이 파일이 존재하면 Python은 해당 디렉토리를 패키지로 간주하고
그 안에 있는 모듈들을 import할 수 있게 된다.
간단히 말하자면, 현재 tests 디렉토리 안에 본 파일인 __init__.pyt가
있는데, 이게 있음으로 다른 모듈에서 tests 디렉토리 안의
모듈들에 대하여 다음과 같은 형식으로 import가 가능하다.

ex)
from tests import some_test_module

주로 빈 파일로 남겨두지만, 필요에 따라서 초기화 코드나 설정을
포함할 수도 있다.
예컨데, 프로젝트의 다른 부분에서 특정 테스트 유틸리티나 헬퍼 함수를
사용하고자 한다면, 위와 같이 쉽게 import 하여 접근할 수 있는 것이다.
또한 테스트 프레임 워크(ex. pytest)에서 테스트를 자동으로 발견하고
실행하는 데에도 도움이 된다.

pytest의 경우 test_로 시작하거나 _test로 끝나는 함수들을 자동으로 
발견하고 실행한다. 다만, __init__.py 파일이 없어도 pytest는 테스트 파일을
발견하고 실행할 수 있긴하다. 하지만 해당
테스트 파일에서 본 tests/ 폴더를 패키지로 인식해서 import하여 불러오려면
본 파일과 같이 해당 디렉토리에 __init__.py가 있어야 한다. 
즉, __init__.py 파일은 주로 테스트 코드의 모듈화와 재사용성을 높이기 위해 
사용되는 것이다.

"""
