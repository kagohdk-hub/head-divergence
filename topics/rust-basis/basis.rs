//// 型 ////
// 整数型
42i32   // i32型で42
42u64   // u64型で42
// 浮動小数点型
3.14f32
3.14f64
// 文字列型
str::string::String // utf-8 エンコードされ長さ変更可能な文字列型
// 配列とスライス
[i32; 500]  // 要素数500で要素型がi32な配列
&[i32]  // i32配列へのスライス  スライス=配列などの連続した領域への参照
// 可変長配列
let mut vec = Vec::new();
vec.push(1);
vec.push(2);

vec.[0];
// ユニット = 要素が一つもないタプル
()
// カスタム型 = 複数の値や型をまとめて扱うことができる型
//// Cスタイル
struct CStyleColor {
    red: u8,
    green: u8,
    blue: u8,
}
//// タプルスタイルで色を管理する型
struct TupleStyleColor(u8, u8, u8);
//// ユニットスタイルの構造体
struct UnitStyle;

// Enum型
enum Color {
    CStyleRgb { red: u8, green: u8, blue: u8 },
    TupleStyleRgb(u8, u8, u8),
    UnitStyleWhite,
}
std::result::Result<T, E>  // Result<T, E> は成功と失敗を表すことのできるenum
    // rust には例外はない。代わりにResult<T, E>を返す
    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
do_something()?;    // 失敗する可能性がある処理do_somethingを呼び出す
    // ここで ? がついている式がErrの値を持っている場合、その値をそのまま返す
    // 以下と等価
    if let Err(e) = do_something() {
        return Err(e);
    }
std::option::Option<T>  // Optionは値を持つことと持たないことを表すことのできるenum
    enum Option<T> {
        None,
        Some(T),
    }
// tuple
(i32, String, f64)

// 変数
let number = 1;
let number: i32 = 1;    // 型を明示
//// 変数のデフォルトは不変(immutable)
let mut number = 1; // 値の変更が必要な場合は mut をつける

// 型推論
let number = 1u64;
// この number は u64 の値を代入しているのでu64と推論される。
// rustの型推論はあとからどのように使われるか、からも推論してくれる。
let mut vec = Vec::new();
vec.push(1u64);
    // ここでは1行目のvecの型は2行目からu64と推論してくれる。
    //  >>　推論してくれるから、静的型付け言語でありながら、型をあまり書くことなく記述できる

// 条件分岐
if value == 42 {
    ...
} else if value2 == 500 {
    ...
} else {
    ...
}

// loop
loop {
    ...
    if break_loop_condition {
        break;
    }
    if continue_loop_condition {
        continue;
    }
}
let mut counter = 0;
while counter < 100 {
    counter += 1;
}
for n in 0..100 {
    ...
}

// 関数
fn add_number(a: i32, b: i32) -> i32 {
    a + b
}
fn add_number(a: i32, b: i32) -> i32 {
    return a + b;
}

// main
fn main() {
    ...
}
// プログラムの開始地点となる関数


//// ここから モジュールと可視性 / 所有権とムーブ / 借用 など rust の特徴的なところが出てくる
