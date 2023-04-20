

# Coordinator-ParallelismListener 设计文档

## 1. 概述

Coordinator-ParallelismListener 是一个在集群及资源队列维度，用于监控 Spark 应用程序计算并行度的工具，可以实时获取当前 Spark 作业的实际计算并行度，同时收集 Spark 的 Metrics 以监控当前集群中所有 Spark 作业的计算并行度情况。

## 2. 主要功能

- 监听 Spark 作业并获取实际计算并行度。
- 收集 Spark Metrics 并监控当前集群中所有 Spark 作业的计算并行度情况。
- 计算并行度：指当前实际有多少作业在并行运行。
- 后台进程：一次启动即可实时监控所在集群的所有 Spark 应用。
- 基于 Java 实现。

## 3. 接口描述

Coordinator-ParallelismListener 提供以下接口：

- `start()` : 启动 Coordinator-ParallelismListener 进程以监听 Spark 应用程序。
- `stop()` : 停止 Coordinator-ParallelismListener 进程。

## 4. 主要流程

## 5. Coordinator-ParallelismListener 的主要流程如下：

1. 通过与 Spark Driver 程序的交互，监听 Spark 应用程序并获取应用程序的相关信息，包括应用程序的 ID，应用程序的运行状态等。
2. 监控 Spark Metrics，收集 Spark 应用程序的计算并行度情况，并将其存储到本地文件中。
3. 根据收集的计算并行度信息，计算当前集群中所有 Spark 应用程序的计算并行度。
4. 定期将计算并行度的结果写入到本地文件中，以供查询和分析。
5. 当 Coordinator-ParallelismListener 进程停止时，清除所有已经收集的信息，关闭所有相关的资源。

以下是 Coordinator-ParallelismListener 的完整模块化设计：

### 1. 监听模块

### Spark 应用程序监听器

- 负责监听 Spark 应用程序。
- 获取应用程序的相关信息，包括应用程序的 ID，应用程序的运行状态等。
- 将应用程序信息发送给 Spark 应用程序管理器进行管理。

### Spark 应用程序管理器

- 负责管理所有正在运行的 Spark 应用程序。
- 维护每个应用程序的信息，包括应用程序的 ID，应用程序的运行状态等。
- 可以根据应用程序的 ID 查询应用程序的状态。

### 2. Metric 收集模块

### Spark Metrics 收集器

- 负责收集 Spark 应用程序的计算并行度情况。
- 使用 Spark 的 Metrics 组件进行数据收集，并将数据存储到 Metric 数据库中。

### Metric 数据库

- 用于存储收集到的 Spark Metrics。
- 可以根据应用程序的 ID 查询应用程序的计算并行度情况。

### 3. 计算并行度模块

### 并行度计算器

- 负责根据收集的计算并行度信息，计算当前集群中所有 Spark 应用程序的计算并行度。
- 可以通过调用 Metric 数据库获取应用程序的计算并行度情况。

### 4. 文件存储模块

### 并行度结果存储器

- 负责将计算并行度的结果写入到本地文件中，以供查询和分析。

### 5. 控制模块

### Coordinator-ParallelismListener 控制器

- 提供 start() 和 stop() 接口，以便用户进行控制。
- 可以启动监听模块，Metric 收集模块，计算并行度模块和文件存储模块。
- 可以停止监听模块，Metric 收集模块，计算并行度模块和文件存储模块。

### 6. 指标展示模块

### 指标收集器

- 负责从本地文件中读取计算并行度的结果，将其转化为 Prometheus 可以理解的格式，并将指标数据推送给 Prometheus。

### 存储模块

- 将指标数据存储到 Prometheus 数据库中，以供 Grafana 进行查询和展示。

### Grafana 配置模块

- 配置 Grafana 的数据源，将 Prometheus 数据库添加为数据源，并配置相应的 Dashboard，用于展示 Coordinator-ParallelismListener 的指标数据。

### 启动方式

- 增加一个启动方式，用于启动指标收集器和存储模块，以便将 Coordinator-ParallelismListener 的指标数据推送给 Prometheus。

通过以上模块的实现，可以将 Coordinator-ParallelismListener 进一步拓展，增加指标展示功能，为用户提供


## 6. 启动方式

Coordinator-ParallelismListener 可以像 Spark History Server 一样启动。用户可以通过以下命令来启动 Coordinator-ParallelismListener：

```
$ bin/start-coordinator.sh
```

该命令会启动一个后台进程来监听 Spark 应用程序，并将监控结果存储到本地文件中。

## 7. 与 Spark Server 端的交互

Coordinator-ParallelismListener 与 Spark Server 端通过 REST API 进行交互，以获取应用程序的相关信息。在启动 Coordinator-ParallelismListener 进程时，需要配置 Spark Server 的地址和端口号。

## 8. 总结

Coordinator-ParallelismListener 是一个用于监控 Spark 应用程序计算并行度的工具，可以实时获取当前 Spark 作业的实际计算并行度，并收集 Spark Metrics 以监控当前集群中所有 Spark 作业的计算并行度情况。该工具是一个后台进程，一次启动即可实时监控所在集群的所有 Spark 应用，并提供了 start() 和 stop() 接口以