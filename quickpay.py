from yoomoney import Quickpay, Client
from uuid import uuid4
from time import sleep


client = Client(
    token="YOUR_TOKEN"
)

label = str(uuid4())

quickpay = Quickpay(
    receiver="YOUR_RECEIVER",
    quickpay_form="example",
    targets="example",
    paymentType="example",
    sum=2,
    label=label
)

print(quickpay.base_url, quickpay.redirected_url, sep="\n")

history = client.operation_history(label=label)

start = True
while start:
    sleep(10)
    for operation in history.operations:
        if operation.status == "success":
            start = False
            print("Оплпата прошла успешно")
        else:
            print("Оплата не прошла")
