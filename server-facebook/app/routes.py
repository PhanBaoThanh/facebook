import os
from app import app, db
from flask import redirect, render_template, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify, send_from_directory, send_file
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app.models import NguoiDung,Nhom,ThanhVienNhom,TinNhan
from app.Service import NguoiDungService,NhomService,AdminService,BaiDangCaNhanService,BaiDangNhomService,BinhLuanBaiDangCaNhanService,BinhLuanBaiDangNhomService,CamXucBaiDangCaNhanService,CamXucBaiDangNhomService,FriendService,ThanhVienNhomService,TinNhanService,XetDuyetBaiDangNhomService,YeuCauKetBanService,YeuCauThamGiaNhomService
import json
from datetime import datetime
from app.ViewService import main



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/img/<path:filename>')
def serve_image(filename):          
    return send_from_directory(app.config["GET_FOLDER"], filename)

# ===================================================================================================== #
# Admin:
@app.route('/admin',methods=['POST'])
def createAdmin():
    AdminForm = request.get_json()
    Admin = AdminService.createAdmin(username = AdminForm['taikhoan'],
                                     password = AdminForm['matkhau'],
                                     name= AdminForm['hoten'],
                                     dayOfBirth=AdminForm['ngaysinh'])
    if Admin is None:
        return "Create Admin Fail",500
    return "Create Admin Success", 201
    
@app.route('/admin-update',methods=['POST'])
def updateAdmin():
    AdminForm = request.get_json()
    Admin = AdminService.updateAdmin(username = AdminForm['taikhoan'],
                                     password = AdminForm['matkhau'],
                                     name= AdminForm['hoten'],
                                     dayOfBirth=AdminForm['ngaysinh'])
    if Admin is None:
        return "Update Admin Fail",500
    return "Update Admin Success", 201

@app.route('/admin/<int:admin_id>', methods=['DELETE'])
def deleteAdmin(admin_id):
    AdminService.deleteAdmin(id = admin_id)
    return "Delete admin Success", 200

@app.route('/admin/login', methods = ['POST'])
def adminLogin():
    loginInfo = request.get_json()
    username = loginInfo['username']
    password = loginInfo['password']
    admin = AdminService.checkLogin(username=username, password=password)
    if admin is None:
        return "Wrong Username/Password", 200
    login_user(admin)
    return jsonify(admin.serialize())

@app.route('/admin/logout', methods = ["GET"])
def adminLogout():
    logout_user()
    return "Admin Logged Out", 200

@app.route('/test',methods=['GET'])
def test():
    return main.test()

@app.route('/view1/client_id',methods=['GET'])
def getView1(client_id):
    return json.dumps(main.GetAllBaiDangCaNhan(client_id),indent=4)

@app.route('/view',methods=['GET'])
def getView():
    clientId = request.get_json()
    return json.dumps(main.GetAllBaiDangCaNhanByMaNguoiDung(clientId['maNguoiDung']),indent=4)
    
        
    

# ===================================================================================================== #
# Bài đăng cá nhân:
@app.route('/post-client',methods=['POST'])
def createPostClient():
    PostClientForm = request.form()
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    PostClient = BaiDangCaNhanService.createBaiDangCaNhan(
        manguoidung = PostClientForm['manguoidung'],
        noidung = PostClientForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if PostClient is None:
        return "Create Post Client Fail",500
    return "Create Post Client Success", 201
    
@app.route('/post-client-update',methods=['POST'])
def updatePostClient():
    PostClient = request.form()
    Img = request.files['image']
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    PostClient = BaiDangCaNhanService.updateBaiDangCaNhan(
        mabaidangcanhan = PostClientForm['mabaidangcanhan'],
        noidung = PostClientForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if PostClient is None:
        return "Update Post Client Fail",500
    return "Update Post Client Success", 201

@app.route('/get-all-post-client-by-client-id/<int:client_id>',methods=['GET'])
def getAllPostClientByClientId(client_id):
    PostClients = BaiDangCaNhanService.getAllBaiDangCaNhanByMaNguoiDung(manguoidung=client_id)
    list = []
    for PostClient in PostClients:
        list.append(PostClient.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-client-find-by-id/<int:post_client_id>',methods=['GET'])
def findPostClientById(post_client_id):
    return jsonify(BaiDangCaNhanService.findBaiDangCaNhanById(post_client_id).serialize())

@app.route('/post-client-find-by-key',methods=['GET'])
def findPostClientByKey():
    key = request.get_json()
    PostClients = BaiDangCaNhanService.findBaiDangCaNhanByKey(key = key['key'])
    list = []
    for PostClient in PostClients:
        list.append(PostClient.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-client/<int:post_client_id>', methods=['DELETE'])
def deletePostClient(post_client_id):
    BaiDangCaNhanService.deleteBaiDangCaNhan(id = post_client_id)
    return "Delete Post Client Success", 201



# ===================================================================================================== #
# Bài đăng nhóm:
@app.route('/post-group',methods=['POST'])
def createPostGroup():
    PostGroupForm = request.form()
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    PostGroup = BaiDangNhomService.createBaiDangNhom(
        manhom = PostGroupForm['manhom'],
        manguoidung = PostGroupForm['manguoidung'],
        noidung = PostGroupForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if PostGroup is None:
        return "Create Post Group Fail",500
    return "Create Post Group Success", 201
    
@app.route('/post-group-update',methods=['POST'])
def updatePostGroup():
    PostGroupForm = request.form()
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    PostGroup = BaiDangNhomService.updateBaiDangNhom(
        mabaidangnhom = PostGroupForm['mabaidangnhom'],
        noidung = PostGroupForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if PostGroup is None:
        return "Update Post Group Fail",500
    return "Update Post Group Success", 201

@app.route('/get-all-post-group-by-group-id/<int:group_id>',methods=['GET'])
def getAllPostGroupByGroupId(group_id):
    PostGroups = BaiDangNhomService.getAllBaiDangNhomByMaNhom(manhom = group_id)
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-group-find-by-id/<int:post_group_id>',methods=['GET'])
def findPostGroupById(post_group_id):
    return jsonify(BaiDangNhomService.findBaiDangNhomById(id = post_group_id).serialize())

@app.route('/post-group-find-by-key',methods=['GET'])
def findPostGroupByKey():
    key = request.get_json()
    PostGroups = BaiDangNhomService.findBaiDangNhomByKey(key = key['key'])
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-group-find-by-client-id',methods=['GET'])
def findPostGroupByClientId():
    PostGroupForm = request.get_json()
    PostGroups = BaiDangNhomService.findBaiDangNhomByMaNguoiDung(manhom = PostGroupForm['manhom'],manguoidung = PostGroupForm['manguoidung'])
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-group/<int:post_group_id>', methods=['DELETE'])
def deletePostGroup(post_group_id):
    BaiDangNhomService.deleteBaiDangNhom(id = post_group_id)
    return "Delete Post Group Success", 201


# ===================================================================================================== #
# Bình luận bài đăng cá nhân:
@app.route('/comment-client',methods=['POST'])
def createCommentClient():
    CommentClientForm = request.get_json()
    CommentClient = BinhLuanBaiDangCaNhanService.createBinhLuanBaiDangCaNhan(
        mabaidang= CommentClientForm['mabaidang'],
        manguoidung = CommentClientForm['manguoidung'],
        noidung = CommentClientForm['noidung']
    )
    if CommentClient is None:
        return "Create Comment Client Fail",500
    return "Create Comment Client Success", 201
    
@app.route('/comment-client-update',methods=['POST'])
def updateCommentClient():
    CommentClientForm = request.get_json()
    CommentClient = BinhLuanBaiDangCaNhanService.updateBinhLuanBaiDangCaNhan(
        mabinhluanbaidangcanhan= CommentClientForm['mabinhluanbaidangcanhan'],
        noidung = CommentClientForm['noidung']
    )
    if CommentClient is None:
        return "Update Comment Client Fail",500
    return "Update Comment Client Success", 201

@app.route('/get-all-comment-client-by-post-id/<int:post_id>',methods=['GET'])
def getAllCommentClientByPostId(post_id):
    CommentClients = BinhLuanBaiDangCaNhanService.getAllBinhLuanBaiDangCaNhanByMaBaiDang(mabaidang = post_id)
    list = []
    for CommentClient in CommentClients:
        list.append(CommentClient.serialize())
    return json.dumps(list,indent=4)

@app.route('/comment-client-find-by-id/<int:comment_client_id>',methods=['GET'])
def findCommentClientById(comment_client_id):
    return jsonify(BinhLuanBaiDangCaNhanService.findBinhLuanBaiDangCaNhanById(id = comment_client_id).serialize())

@app.route('/comment-client/<int:comment_client_id>', methods=['DELETE'])
def deleteCommentClient(comment_client_id):
    BinhLuanBaiDangCaNhanService.deleteBinhLuanBaiDangCaNhan(id = comment_client_id)
    return "Delete Comment Client Success", 201


# ===================================================================================================== #
# Bình luần bài đăng nhóm:
@app.route('/comment-group',methods=['POST'])
def createCommentGroup():
    CommentGroupForm = request.get_json()
    CommentGroup = BinhLuanBaiDangNhomService.createBinhLuanBaiDangNhom(
        manhom = CommentGroupForm['manhom'],
        mabaidang = CommentGroupForm['mabaidang'],
        manguoidung = CommentGroupForm['manguoidung'],
        noidung = CommentGroupForm['noidung']
    )
    if CommentGroup is None:
        return "Create Comment Group Fail",500
    return "Create Comment Group Success", 201
    
@app.route('/comment-group-update',methods=['POST'])
def updateCommentGroup():
    CommentGroupForm = request.get_json()
    CommentGroup = BinhLuanBaiDangNhomService.updateBinhLuanBaiDangNhom(
        mabinhluanbaidangnhom = CommentGroupForm['mabinhluanbaidangnhom'],
        noidung = CommentGroupForm['noidung']
    )
    if CommentGroup is None:
        return "Update Comment Group Fail",500
    return "Update Comment Group Success", 201

@app.route('/get-all-comment-group-by-post-id',methods=['GET'])
def getAllCommentGroupByPostId():
    CommentGroupForm = request.form()
    CommentGroups = BinhLuanBaiDangNhomService.getAllBinhLuanBaiDangNhomByMaBaiDang(mabaidang = CommentGroupForm['mabaidang'],manhom=CommentGroupForm['manhom'])
    list = []
    for CommentGroup in CommentGroups:
        list.append(CommentGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/comment-group-find-by-id/<int:comment_group_id>',methods=['GET'])
def findCommentGroupById(comment_group_id):
    return jsonify(BinhLuanBaiDangNhomService.findBinhLuanBaiDangNhomById(id = comment_group_id))

@app.route('/comment-group/<int:comment_group_id>', methods=['DELETE'])
def deleteCommentGroup(comment_group_id):
    BinhLuanBaiDangNhomService.deleteBinhLuanBaiDangNhom(id = comment_group_id)
    return "Delete Comment Group Success", 201


# ===================================================================================================== #
# Cảm xúc bài đăng cá nhân:
@app.route('/client-reaction',methods=['POST'])
def createClientReaction():
    ClientReactionForm = request.get_json()
    ClientReaction = CamXucBaiDangCaNhanService.createCamXucBaiDangCaNhan(
        mabaidang = ClientReactionForm['mabaidang'],
        manguoidung = ClientReactionForm['manguoidung']
    )
    if ClientReaction is None:
        return "Create Client Reaction Fail",500
    return "Create Client Reaction Success", 201
    
@app.route('/client-reaction-get-count-by-post-id/<int:post_id>',methods=['GET'])    
def getCountClientReactionByPostId(post_id):
    count = CamXucBaiDangCaNhanService.getCountByMaBaiDang(mabaidang = post_id)
    return {
        'count': count
    }
    
@app.route('/client-reaction-get-all-by-post-id/<int:post_id>',methods=['GET'])
def getAllClientReactionByPostId(post_id):
    ClientReactions = CamXucBaiDangCaNhanService.getAllCamXucBaiDangCaNhanByMaBaiDang(mabaidang = post_id)
    list = []
    for ClientReaction in ClientReactions:
        list.append(ClientReaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/client-reaction-get-all-by-client-id/<int:client_id>',methods=['GET'])
def getAllClientReactionByClientId(client_id):
    ClientReactions = CamXucBaiDangCaNhanService.getAllCamXucBaiDangCaNhanByMaNguoiDung(manguoidung = client_id)
    list = []
    for ClientReaction in ClientReactions:
        list.append(ClientReaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/client-reaction-find-by-id/<int:client_reaction_id>',methods=['GET'])
def findClientReactionById(client_reaction_id):
    return jsonify(CamXucBaiDangCaNhanService.findCamXucBaiDangCaNhanById(id=client_reaction_id))

@app.route('/client-reaction/<int:client_reaction_id>', methods=['DELETE'])
def deleteClientReaction(client_reaction_id):
    CamXucBaiDangCaNhanService.deleteCamXucBaiDangCaNhan(id = client_reaction_id)
    return "Delete Client Reaction Success", 201

# ===================================================================================================== #
# Cảm xúc bài đăng nhóm:
@app.route('/group-reaction',methods=['POST'])
def createGroupReaction():
    GroupReactionForm = request.get_json()
    GroupReaction = CamXucBaiDangNhomService.createCamXucBaiDangNhom(
        manhom = GroupReactionForm['manhom'],
        mabaidang = GroupReactionForm['mabaidang'],
        manguoidung = GroupReactionForm['manguoidung']
    )
    if GroupReaction is None:
        return "Create Group Reaction Fail",500
    return "Create Group Reaction Success", 201
    
@app.route('/group-reaction-get-count-by-post-id',methods=['GET'])    
def getCountGroupReactionByPostId():
    GroupReactionForm = request.get_json()
    count = CamXucBaiDangNhomService.getCountByMaBaiDang(manhom = GroupReactionForm['manhom'],mabaidang=GroupReactionForm['mabaidang'])
    return {
        'count': count
    }
    
@app.route('/group-reaction-get-all-by-post-id/<int:post_id>',methods=['GET'])
def getAllGroupReactionByPostId(post_id):
    GroupReactions = CamXucBaiDangNhomService.getAllCamXucBaiDangNhomByMaBaiDang(id = post_id)
    list = []
    for GroupReaction in GroupReactions:
        list.append(GroupReaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/group-reaction-get-all-by-client-id/<int:client_id>',methods=['GET'])
def getAllGroupReactionByClientId(client_id):
    GroupReactions = CamXucBaiDangNhomService.getAllCamXucBaiDangNhomByMaNguoiDung(manguoidung = client_id)
    list = []
    for GroupReaction in GroupReactions:
        list.append(GroupReaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/group-reaction-find-by-id/<int:group_reaction_id>',methods=['GET'])
def findGroupReactionById(group_reaction_id):
    return jsonify(CamXucBaiDangNhomService.findCamXucBaiDangNhomById(id = group_reaction_id).serialize())

@app.route('/group-reaction/<int:group_reaction_id>', methods=['DELETE'])
def deleteGroupReaction(group_reaction_id):
    CamXucBaiDangNhomService.deleteCamXucBaiDangNhom(id = group_reaction_id)
    return "Delete Group Reaction Success", 201


# ===================================================================================================== #
# Friend:
@app.route('/friend',methods=['POST'])
def createFriend():
    FriendForm = request.get_json()
    Friend = FriendService.createFriend(manguoidung1 = FriendForm['manguoidung1'],manguoidung2=FriendForm['manguoidung2'])
    if Friend is None:
        return "Create Friend Fail",500
    return "Create Friend Success", 201

@app.route('/get-all-friend-by-client-id/<int:client_id>',methods=['GET'])
def getAllFriendByClientId(client_id):
    Friends = FriendService.findFriendByMaNguoiDung(manguoidung = client_id)
    list = []
    for Friend in Friends:
        list.append(Friend.serialize())
    return json.dumps(list,indent=4)

@app.route('/friend-find-by-id/<int:friend_id>',methods=['GET'])
def findFriendById(friend_id):
    return jsonify(FriendService.findFriendById(id = friend_id).serialize())

@app.route('/friend/<int:friend_id>', methods=['DELETE'])
def deleteFriend(friend_id):
    FriendService.deleteFriend(id = friend_id)
    return "Delete Friend Success", 201


# ===================================================================================================== #
# Người dùng:
@app.route('/client', methods = ['POST'])
def createClient():
    ClientForm = request.form
    ClientAvt = request.files['avt']
    ClientBackgroundImg = request.files['backgroundImage']

    if ClientAvt.filename is None:
        flash('No Avatar uploaded')
    elif ClientBackgroundImg.filename is None:
        flash('No Background Image uploaded')
    elif ClientAvt and allowed_file(ClientAvt.filename) and ClientBackgroundImg and allowed_file(ClientBackgroundImg.filename):
        filenameAvt = secure_filename(ClientAvt.filename)
        pathAvt = os.path.join(app.config['UPLOAD_FOLDER'],filenameAvt)
        ClientAvt.save(pathAvt)
        filenameBackgroundImg = secure_filename(ClientBackgroundImg.filename)
        pathBackgroundImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameBackgroundImg)
        ClientBackgroundImg.save(pathBackgroundImg)
    datetime_object = datetime.strptime(ClientForm['ngaysinh'],'%Y-%m-%d').date()
    Client = NguoiDungService.createNguoiDung(
        hoten =ClientForm['hoten'],
        sdt=ClientForm['sdt'],
        email=ClientForm['email'],
        taikhoan=ClientForm['taikhoan'],
        matkhau=ClientForm['matkhau'],
        gioitinh=True if ClientForm['gioitinh'] == 'true' else False,
        ngaysinh=datetime_object,
        anh=ClientAvt.filename,
        anhbia=ClientBackgroundImg.filename
    )
    if Client is None:
        return "Create Client Fail",500
    return jsonify(Client.serialize())

@app.route("/client-update", methods = ["POST"])
def updateClient():
    ClientForm = request.get_json()
    datetime_object = datetime.strptime(ClientForm['ngaysinh'],'%Y-%m-%d').date()
    Client = NguoiDungService.updateNguoiDung(hoten = ClientForm['hoten'],
                                              sdt = ClientForm['sdt'],
                                              email = ClientForm['email'],
                                              taikhoan = ClientForm['taikhoan'],
                                              gioitinh=True if ClientForm['gioitinh'] == 'true' else False,
                                              ngaysinh = datetime_object)
    if Client is None:
        return "Update client fail", 500
    return "Update client Success", 201

@app.route('/client-password', methods =['POST'])
def updatePassword():
    ClientForm = request.get_json()
    Client = NguoiDungService.updatePassword(taikhoan = ClientForm['taikhoan'],matkhau = ClientForm['matkhau'])
    if Client is None:
        return 'Update password fail',500
    return 'Update password success',201
    

@app.route("/client-avt", methods = ["POST"])
def updateAvtClient():
    ClientForm = request.form
    Avt = request.files['avt']
    if Avt.filename is None:
        flash('No avatar uploaded')
    elif Avt and allowed_file(Avt.filename):
        AvtFilename = secure_filename(Avt.filename)
        AvtPath = os.path.join(app.config['UPLOAD_FOLDER'],AvtFilename)
        Avt.save(AvtPath)
        
    Client = NguoiDungService.updateAvatar(taikhoan = ClientForm['taikhoan'],avt=Avt.filename)
    if Client is None:
        return "Update avatar client fail", 500
    return "Update avatar client Success", 201

@app.route("/client-backgroundImg", methods = ["POST"])
def updateBackgroundImageClient():
    ClientForm = request.form
    Img = request.files['backgroundImg']
    if Img.filename is None:
        flash('No background image uploaded')
    elif Img and allowed_file(Img.filename):
        ImgFilename = secure_filename(Img.filename)
        ImgPath = os.path.join(app.config['UPLOAD_FOLDER'],ImgFilename)
        Img.save(ImgPath)
        
    Client = NguoiDungService.updateBackgroundImage(taikhoan = ClientForm['taikhoan'],backgroundImg=Img.filename)
    if Client is None:
        return "Update background image client fail", 500
    return "Update background image client Success", 201

@app.route('/client-find/<int:client_id>',methods=['GET'])
def findClientById(client_id):
    return jsonify(NguoiDungService.findNguoiDungById(id = client_id).serialize())

@app.route('/client-search',methods=['GET'])
def searchClientByKey():
    key = request.get_json()
    Clients = NguoiDungService.searchNguoiDung(key = key['key'])
    list = []
    for client in Clients:
        list.append(client.serialize())
    return json.dumps(list,indent=4)

@app.route('/client/<int:client_id>', methods=['DELETE'])
def deleteClient(client_id):
    NguoiDungService.deleteNguoiDung(id = client_id)
    return "Delete client Success", 200

@app.route('/client/login', methods = ['POST'])
def clientLogin():
    loginInfo = request.get_json()
    Client = NguoiDungService.checkLoginNguoiDung(taikhoan = loginInfo['taikhoan'],matkhau= loginInfo['matkhau'])
    if Client is None:
        return "Wrong Username/Password", 500
    login_user(Client)
    return jsonify(Client.serialize())

@app.route('/client/logout', methods = ["GET"])
def clientLogout():
    logout_user()
    return "Client Logged Out", 200

# ===================================================================================================== #
# Nhóm:
@app.route('/group', methods=['POST'])
def createGroup():
    GroupForm = request.form
    GroupAvt = request.files['avt']
    GroupBackgroundImg = request.files['backgroundImage']

    if GroupAvt.filename is None:
        flash('No Avatar uploaded')
    elif GroupBackgroundImg.filename is None:
        flash('No Background Image uploaded')
    elif GroupAvt and allowed_file(GroupAvt.filename) and GroupBackgroundImg and allowed_file(GroupBackgroundImg.filename):
        filenameAvt = secure_filename(GroupAvt.filename)
        pathAvt = os.path.join(app.config['UPLOAD_FOLDER'],filenameAvt)
        GroupAvt.save(pathAvt)
        filenameBackgroundImg = secure_filename(GroupBackgroundImg.filename)
        pathBackgroundImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameBackgroundImg)
        GroupBackgroundImg.save(pathBackgroundImg)
    
    Group = NhomService.createNhom(maquantrivien= GroupForm['maquantrivien'],
                                   tennhom = GroupForm['tennhom'],
                                   anh=GroupAvt.filename,
                                   anhbia=GroupBackgroundImg.filename,
                                   riengtu= GroupForm['riengtu'])
    if Group is None:
        return 'Create Group Fail',500
    return 'Create Product Success',201

@app.route("/group/<int:group_id>", methods = ["POST"])
def updateGroup(group_id):
    GroupForm = request.get_json()
    Group = NhomService.updateNhom(manhom = group_id, tennhom = GroupForm['tennhom'],riengtu = GroupForm['riengtu'])
    if Group is None:
        return "Update group fail", 500
    return "Update group Success", 201

@app.route("/group-avt/<int:group_id>", methods = ["POST"])
def updateAvtGroup(group_id):
    Avt = request.files['avt']
    if Avt.filename is None:
        flash('No avatar uploaded')
    elif Avt and allowed_file(Avt.filename):
        AvtFilename = secure_filename(Avt.filename)
        AvtPath = os.path.join(app.config['UPLOAD_FOLDER'],AvtFilename)
        Avt.save(AvtPath)
        
    Group = NhomService.updateAvatar(manhom = group_id, avt=Avt.filename)
    if Group is None:
        return "Update avatar group fail", 500
    return "Update avatar group Success", 201

@app.route("/group-backgroundImg/<int:group_id>", methods = ["POST"])
def updateBackgroundImageGroup(group_id):
    Img = request.files['backgroundImg']
    if Img.filename is None:
        flash('No background image uploaded')
    elif Img and allowed_file(Img.filename):
        ImgFilename = secure_filename(Img.filename)
        ImgPath = os.path.join(app.config['UPLOAD_FOLDER'],ImgFilename)
        Img.save(ImgPath)
        
    Group = NhomService.updateBackgroundImage(manhom=group_id,backgroundImg=Img.filename)
    if Group is None:
        return "Update background image group fail", 500
    return "Update background image group Success", 201

@app.route('/group-find/<int:group_id>',methods=['GET'])
def findGroupById(group_id):
    return jsonify(NhomService.findNhomById(id = group_id).serialize())

@app.route('/group-search',methods=['GET'])
def searchGroupByKey():
    key = request.get_json()
    Groups = NhomService.searchNhom(key = key['key'])
    list = []
    for group in Groups:
        list.append(group.serialize())
    return json.dumps(list,indent=4)

@app.route('/group/<int:group_id>', methods=['DELETE'])
def deleteGroup(group_id):
    NhomService.deleteNhom(id=group_id)
    return "Delete group Success", 200

# ===================================================================================================== #
# Thành viên nhóm:
@app.route('/group-member',methods=['POST'])
def createGroupMember():
    GroupMemberForm = request.get_json()
    GroupMember = ThanhVienNhomService.createThanhVienNhom(manhom = GroupMemberForm['manhom'],manguoidung= GroupMemberForm['manguoidung'])
    if GroupMember is None:
        return "Create Group Member Fail",500
    return "Create Group Member Success", 201

@app.route('/get-all-group-member-by-group-id/<int:group_id>',methods=['GET'])
def getAllGroupMemberByGroupId(group_id):
    GroupMembers = ThanhVienNhomService.getAllThanhVienNhomByMaNhom(manhom = group_id)
    list = []
    for GroupMember in GroupMembers:
        list.append(GroupMember.serialize())
    return json.dumps(list,indent=4)

@app.route('/group-member-find-by-id/<int:group_member_id>',methods=['GET'])
def findGroupMemberById(group_member_id):
    return jsonify(ThanhVienNhomService.findThanhVienNhomById(id=group_member_id).serialize())

@app.route('/group-member-find-by-client-id/<int:client_id>',methods=['GET'])
def findGroupMemberByClientId(client_id):
    GroupMembers = ThanhVienNhomService.findAllThanhVienNhomByMaNguoiDung(manguoidung = client_id)
    list = []
    for GroupMember in GroupMembers:
        list.append(GroupMember.serialize())
    return json.dumps(list,indent=4)

@app.route('/group-member/<int:group_member_id>', methods=['DELETE'])
def deleteGroupMember(group_member_id):
    ThanhVienNhomService.deleteThanhVienNhom(id = group_member_id)
    return "Delete Group Member Success", 201

# ===================================================================================================== #
# Tin nhắn:
@app.route('/message',methods=['POST'])
def createMessage():
    MessageForm = request.get_json()
    Message = TinNhanService.createTinNhan(
        nguoigui= MessageForm['nguoigui'],
        nguoinhan = MessageForm['nguoinhan'],
        noidung = MessageForm['noidung']
    )
    if Message is None:
        return "Create Message Fail",500
    return "Create Message Success", 201

@app.route('/get-all-message-by-client-id',methods=['GET'])
def getAllMessageByClientId():
    MessageForm = request.get_json()
    Message = TinNhanService.getAllTinNhanByMaNguoiDung(nguoidung1 = MessageForm['nguoidung1'],nguoidung2 = MessageForm['nguoidung2'])
    list = []
    for Message in Messages:
        list.append(Message.serialize())
    return json.dumps(list,indent=4)

@app.route('/message-find-by-id/<int:message_id>',methods=['GET'])
def findMessageById(message_id):
    return jsonify(TinNhanService.findTinNhanById(id=message_id).serialize())

@app.route('/message/<int:message_id>', methods=['DELETE'])
def deleteMessage(message_id):
    TinNhanService.deleteTinNhan(id = message_id)
    return "Delete Message Success", 201

# ===================================================================================================== #
# Xét duyệt bài đăng nhóm:
@app.route('/confirm-post',methods=['POST'])
def createConfirmPost():
    ConfirmPostForm = request.form()
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    ConfirmPost = XetDuyetBaiDangNhomService.createXetDuyetBaiDangNhom(
        manhom = PostGroupForm['manhom'],
        manguoidung = PostGroupForm['manguoidung'],
        noidung = PostGroupForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if ConfirmPost is None:
        return "Create Confirm Post Fail",500
    return "Create Confirm Post Success", 201

@app.route('/get-all-confirm-post-by-group-id/<int:group_id>',methods=['GET'])
def getAllConfirmPostByGroupId(group_id):
    ConfirmPosts = XetDuyetBaiDangNhomService.getAllXetDuyetBaiDangNhomByMaNhom(manhom = group_id)
    list = []
    for ConfirmPost in ConfirmPosts:
        list.append(ConfirmPost.serialize())
    return json.dumps(list,indent=4)

@app.route('/confirm-post-find-by-id/<int:confirm_post_id>',methods=['GET'])
def findConfirmPostById(confirm_post_id):
    return jsonify(XetDuyetBaiDangNhomService.findXetDuyetBaiDangNhomById(id = confirm_post_id).serialize())

@app.route('/confirm-post/<int:confirm_post_id>', methods=['DELETE'])
def deleteConfirmPost(confirm_post_id):
    XetDuyetBaiDangNhomService.deleteXetDuyetBaiDangNhom(id = confirm_post_id)
    return "Delete Confirm Post Success", 201

@app.route('/confirmed-post/<int:confirm_post_id>',methods=['POST'])
def confirmedPost(confirm_post_id):
    ConfirmPost = XetDuyetBaiDangNhomService.confirmed(id = confirm_post_id)
    if ConfirmPost is None:
        return 'Confirm Post Fail',500
    else:
        return 'Confirm Post Success',201
    

# ===================================================================================================== #
# Yêu cầu kết bạn:
@app.route('/friend-request',methods=['POST'])
def createFriendRequest():
    FriendRequestForm = request.get_json()
    FriendRequest = YeuCauKetBanService.createYeuCauKetBan(nguoinhan = FriendRequestForm['nguoinhan'],nguoigui = FriendRequestForm['nguoigui'])
    if FriendRequest is None:
        return "Create Friend Request Fail",500
    return "Create Friend Request Success", 201

@app.route('/get-all-friend-request-by-receiver/<int:receiver_id>',methods=['GET'])
def getAllFriendRequestByReceiver(receiver_id):
    FriendRequests = YeuCauKetBanService.getAllYeuCauKetBanByMaNguoiNhan(manguoinhan = receiver_id)
    list = []
    for FriendRequest in FriendRequests:
        list.append(FriendRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-friend-request-by-sender/<int:sender_id>',methods=['GET'])
def getAllFriendRequestBySender(sender_id):
    FriendRequests = YeuCauKetBanService.getAllYeuCauKetBanByMaNguoiNhan(manguoinhan = sender_id)
    list = []
    for FriendRequest in FriendRequests:
        list.append(FriendRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/friend-request-find-by-id/<int:friend_request_id>',methods=['GET'])
def findFriendRequestById(friend_request_id):
    return jsonify(YeuCauKetBanService.findYeuCauKetBanById(id = friend_request_id).serialize())

def deleteFriendRequest(friend_request_id):
    YeuCauKetBanService.deleteYeuCauKetBan(id = friend_request_id)
    return "Delete Friend Request Success", 201

# ===================================================================================================== #
# Yêu cầu tham gia nhóm: 
@app.route('/group-request',methods=['POST'])
def createGroupRequest():
    GroupRequestForm = request.get_json()
    GroupRequest = YeuCauThamGiaNhomService.createYeuCauThamGiaNhom(manhom = GroupRequestForm['manhom'],manguoidung = GroupRequestForm['manguoidung'])
    if GroupRequest is None:
        return "Create Group Request Fail",500
    return "Create Group Request Success", 201

@app.route('/get-all-group-request-by-client-id/<int:client_id>',methods=['GET'])
def getAllGroupRequestByReceiver(client_id):
    GroupRequests = YeuCauThamGiaNhomService.getAllYeuCauThamGiaNhomByMaNguoiDung(manguoidung = client_id)
    list = []
    for GroupRequest in GroupRequests:
        list.append(GroupRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-group-request-by-group-id/<int:group_id>',methods=['GET'])
def getAllGroupRequestByGroupId(group_id):
    GroupRequests = YeuCauThamGiaNhomService.getAllYeuCauThamGiaNhomByMaNhom(manhom = group_id)
    list = []
    for GroupRequest in GroupRequests:
        list.append(GroupRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/group-request-find-by-id/<int:group_request_id>',methods=['GET'])
def findGroupRequestById(group_request_id):
    return jsonify(YeuCauThamGiaNhomService.findYeuCauThamGiaNhomById(id = group_request_id).serialize())

def deleteGroupRequest(group_request_id):
    YeuCauThamGiaNhomService.deleteYeuCauThamGiaNhom(id = group_request_id)
    return "Delete Group Request Success", 201
