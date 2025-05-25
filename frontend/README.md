# Flutter

## 布局

#### ✅ Dart 基础（Flutter 的语言）

- 变量、类型、函数、类、泛型、异步（`Future`, `async/await`）

#### ✅ Widget & 布局系统

- 常用布局组件：
  - `Column`, `Row`, `Stack`, `Container`, `Padding`, `Expanded`
- 自适应布局（如 `MediaQuery`, `LayoutBuilder`）
- 自定义组件（Widget 抽取、组合）

#### ✅ 状态管理（最基础的）

- `setState()` 的使用
- 页面跳转与传值：`Navigator.push/pop`、`MaterialPageRoute`
- `InheritedWidget` 概念（为后续状态管理做铺垫）

### 通信

Riverpod

#### ✅ 组件间通信方式

- 父传子：构造函数参数
- 子传父：回调函数（callback）
- 跨组件：状态管理（见下）

#### ✅ 状态管理推荐方案

- 🔥 推荐用 `Riverpod`（简洁且支持模块化）
  - `Provider`, `StateProvider`, `FutureProvider`, `Notifier`
- 其他主流方案：
  - `Provider`（Flutter 官方）
  - `Bloc`, `GetX`, `MobX` 等

### 依赖

```dart
flutter pub get
```

