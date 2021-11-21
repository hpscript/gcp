from google.cloud import bigquery
import matplotlib.pyplot as plt

client = bigquery.Client.from_service_account_json('./client_credentials.json')

QUERY = (
    'SELECT * FROM `gce-test-331622.test.tmcn` ORDER BY timestamp ASC LIMIT 100')
query_job = client.query(QUERY)  
rows = query_job.result()

x = []
y1 = []
y2 = []
for row in rows:
    print(str(row.timestamp)[0:10] + " close:" + str(row.close) + " volume:" + str(row.volume))
    date = str(row.timestamp)[0:10]
    x.append(date)
    y1.append(row.close)
    y2.append(row.volume)

plt.figure(figsize=(10,8))
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

plt.title("tmcn 2021/08/13-2021/11/21")

ax1.plot(x, y1, marker=".", color = "magenta", linestyle = "--")
ax1.set_ylabel('$close-price(pink)$')
ax2.plot(x, y2, marker="o", color = "cyan", linestyle = ":")
ax2.set_ylabel('$trade-volume(blue)$')

plt.savefig('tmcn.jpg',dpi=100)