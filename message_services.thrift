enum MsgType {
    TYPE_A = 1,
    TYPE_B = 2
}

struct Message {
    1: required i64 id;
    2: required MsgType type;
    3: required string body;
}
