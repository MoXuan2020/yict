# yict

此类库只是在编写我的世界中国版模组时，为解决事件传输数据的字典或者本地配置数据的字典和代码中的对象实例进行转换。转换过程只用了递归，在处理数据量庞大的字典或对象实例时，可能会效率低下。

## 温馨提示

请不要添加 __init__ 方法

```python
class Position(object):
  # 正确
  x = None
  y = None
  z = None


class Position(object):
  __init__(self, x, y, z):
    # 错误
    self.x = x
    self.y = y
    self.z = z
```

## 支持类型

|数据类型|
|---|
|int|
|float|
|str|
|bool|
|list|
|tuple|

## 使用方法

```python
from yict import toDict, fromDict


class Position(object):
  x = None
  y = None
  z = None


class Player(object):
  position = None
  dimensionId = None


class World(object):
  playerList = None


position = Position()
position.x = 0
position.y = 0
position.z = 0

player = Player()
player.position = position
player.dimensionId = 0

world = World()
world.playerList = [player]

worldDict = toDict(world)
print(worldDict)
"""
{
    "_m_": "__main__",  // 类所在模块路径
    "_n_": "World",  // 类名称
    "playerList": [
        {
            "_m_": "__main__",
            "_n_": "Player",
            "position": {
                "_m_": "__main__",
                "_n_": "Position",
                "x": 0,
                "y": 0,
                "z": 0
            },
            "dimensionId": 0
        }
    ]
}
"""

worldObj = fromDict(worldDict)
print(worldObj.playerList[0].dimensionId)
"""
0
"""
```
