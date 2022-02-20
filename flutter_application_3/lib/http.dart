import 'package:dio/dio.dart';

const _API_SERVER = "https://webserver-tksgm.run.goorm.io/";

class Server {
  String res = "";

  getReq(url) async {
    Response response;
    Dio dio = new Dio();
    response = await dio.get("$_API_SERVER?url=$url");

    res = response.data.toString();
    print(res);
  }

  resReturn() {
    return res;
  }
}

Server server = Server();
