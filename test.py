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
address = 0
ADDRESS_START = 0  # Modbusアドレスのオフセット調整
ADDRESS_END = 100
  # unitはModbusデバイスIDです。

# 結果を表示
for address in range(ADDRESS_START, ADDRESS_END):
    response = client.read_holding_registers(address, 1, unit=1)
    if not response.isError():
        print(f"Current {address+40001} Value: {response.registers[0]}")

# 接続を閉じる
client.close()