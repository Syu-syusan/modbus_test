from pymodbus.client.tcp import ModbusTcpClient

# 接続設定
HOST = '192.168.85.201'
PORT = 502

# Modbus TCPクライアントのインスタンスを作成
client = ModbusTcpClient(HOST, port=PORT)

# 接続を開始
client.connect()

# 単一のレジスタを読み取り（例: インバータ状態／制御入力命令）
# 40008はModbusアドレスですが、アドレスのオフセットに注意してください。
# pymodbusではアドレスが0から始まるため、1を引いた値を使用する必要があります。
ADDRESS = 40008 - 1  # Modbusアドレスのオフセット調整
result = client.read_holding_registers(ADDRESS, 1, unit=1)  # unitはModbusデバイスIDです。

# 結果を表示
if not result.isError():
    print(f"Value at address {ADDRESS}: {result.registers}")
else:
    print("Error reading register")

# 接続を閉じる
client.close()