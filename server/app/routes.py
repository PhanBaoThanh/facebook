import os
from app import app, db
from flask import redirect, render_template, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename
from app.Service import ClientService,AdminService,CommentService,FriendRequestService,FriendService,GroupMemberService,GroupRequestService,GroupService,MessageService,PostConfirmService,PostService,ReactionService
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
    datetime_object = datetime.strptime(AdminForm['ngaysinh'],'%Y-%m-%d')
    Admin = AdminService.createAdmin(username = AdminForm['taikhoan'],
                                     password = AdminForm['matkhau'],
                                     name= AdminForm['hoten'],
                                     dayOfBirth=datetime_object)
    if Admin is None:
        return "Create Admin Fail",500
    return "Create Admin Success", 201
    
@app.route('/admin-update',methods=['POST'])
def updateAdmin():
    AdminForm = request.get_json()
    datetime_object = datetime.strptime(AdminForm['ngaysinh'],'%Y-%m-%d')
    Admin = AdminService.updateAdmin(username = AdminForm['taikhoan'],
                                     password = AdminForm['matkhau'],
                                     name= AdminForm['hoten'],
                                     dayOfBirth=datetime_object)
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
    admin = AdminService.checkLoginAdmin(username=username, password=password)
    if admin is None:
        return "Wrong Username/Password", 200
    login_user(admin)
    return jsonify(admin.serialize())

@app.route('/admin/logout', methods = ["GET"])
def adminLogout():
    logout_user()
    return "Admin Logged Out", 200

# @app.route('/test',methods=['GET'])
# def test():
#     return main.test()

# @app.route('/view1/client_id',methods=['GET'])
# def getView1(client_id):
#     return json.dumps(main.GetAllBaiDangCaNhan(client_id),indent=4)

# @app.route('/view',methods=['GET'])
# def getView():
#     clientId = request.get_json()
#     return json.dumps(main.GetAllBaiDangCaNhanByMaNguoiDung(clientId['maNguoiDung']),indent=4)
    
        
# ===================================================================================================== #
# Bài đăng:
@app.route('/post',methods=['POST'])
def createPost():
    PostForm = request.form
    check = False
    if request.files['image']:
        Img = request.files['image']
        if Img and allowed_file(Img.filename):
            filenameImg = secure_filename(Img.filename)
            pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
            Img.save(pathImg)
            check = True
        
    Post = PostService.createPost(
        manhom = PostForm['manhom'] if PostForm['manhom'] != 'null' else None,
        manguoidung = PostForm['manguoidung'],
        noidung = PostForm['noidung'],
        anh = Img.filename
    )
    if Post is None:
        return "Create Post Fail",500
    return "Create Post Success", 201

@app.route('/post-no-img',methods=['POST'])
def createPostNoImg():
    PostForm = request.get_json()
    
    Post = PostService.createPost(
        manhom = PostForm['manhom'],
        manguoidung = PostForm['manguoidung'],
        noidung = PostForm['noidung'],
        anh = ''
    )
    if Post is None:
        return "Create Post Fail",500
    return "Create Post Success", 201
    
@app.route('/post-update',methods=['POST'])
def updatePost():
    PostForm = request.form
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    Post = PostService.updatePost(
        mabaidangnhom = PostForm['mabaidangnhom'],
        noidung = PostForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if Post is None:
        return "Update Post Fail",500
    return "Update Post Success", 201

@app.route('/post-update-no-img',methods=['POST'])
def updatePostNoImg():
    PostForm = request.get_json()
    Post = PostService.updatePost(
        mabaidangnhom = PostForm['mabaidangnhom'],
        noidung = PostForm['noidung'],
        anh = ''
    )
    if Post is None:
        return "Update Post Fail",500
    return "Update Post Success", 201

@app.route('/post-find-by-id/<int:post_group_id>',methods=['GET'])
def findPostGroupById(post_group_id):
    return jsonify(PostService.findPostById(id = post_group_id).serialize())

@app.route('/post-find-by-key',methods=['GET'])
def findPostGroupByKey():
    key = request.get_json()
    PostGroups = PostService.findPostByKey(key = key['key'])
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-post-of-client/<int:client_id>',methods=['GET'])
def getAllPostOfClient(client_id):
    Posts = PostService.getAllPostOfClient(clientId = client_id)
    list = []
    for Post in Posts:
        list.append(Post.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-post-of-group/<int:group_id>',methods=['GET'])
def getAllPostGroupOfGroup(group_id):
    PostGroups = PostService.getAllPostOfGroup(manhom = group_id)
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-post-of-friend/<int:client_id>',methods=['GET'])
def getAllPostOfFriend(client_id):
    PostGroups = PostService.getAllPostOfFriend(clientId = client_id)
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-post-by-client-id-and-group-id?clientId=<int:client_id>&groupId=<int:group_id>',methods=['GET'])
def getAllPostGroupByClientId(client_id,group_id):
    PostGroups = PostService.getAllPostByClientIdAndGroupId(manhom = group_id,manguoidung = client_id)
    list = []
    for PostGroup in PostGroups:
        list.append(PostGroup.serialize())
    return json.dumps(list,indent=4)

@app.route('/post/<int:post_group_id>', methods=['DELETE'])
def deletePostGroup(post_group_id):
    PostService.deletePost(id = post_group_id)
    return "Delete Post Group Success", 201


# ===================================================================================================== #
# Bình luận bài đăng cá nhân:
@app.route('/comment',methods=['POST'])
def createComment():
    CommentForm = request.get_json()
    Comment = CommentService.createComment(
        mabaidang= CommentForm['mabaidang'],
        manguoidung = CommentForm['manguoidung'],
        noidung = CommentForm['noidung']
    )
    if Comment is None:
        return "Create Comment Fail",500
    return "Create Comment Success", 201
    
@app.route('/comment-update',methods=['POST'])
def updateComment():
    CommentForm = request.get_json()
    Comment = CommentService.updateComment(
        mabinhluan= CommentForm['mabinhluan'],
        noidung = CommentForm['noidung']
    )
    if Comment is None:
        return "Update Comment Fail",500
    return "Update Comment Success", 201

@app.route('/get-all-comment-by-post-id/<int:post_id>',methods=['GET'])
def getAllCommentByPostId(post_id):
    Comments = CommentService.getAllCommentByPostId(mabaidang = post_id)
    list = []
    for Comment in Comments:
        list.append(Comment.serialize())
    return json.dumps(list,indent=4)

@app.route('/find-comment-by-id/<int:comment_client_id>',methods=['GET'])
def findCommentById(comment_client_id):
    return jsonify(CommentService.findCommentById(id = comment_client_id).serialize())

@app.route('/comment/<int:comment_client_id>', methods=['DELETE'])
def deleteComment(comment_client_id):
    CommentService.deleteComment(id = comment_client_id)
    return "Delete Comment Success", 201


# ===================================================================================================== #
# Cảm xúc bài đăng cá nhân:
@app.route('/reaction',methods=['POST'])
def createReaction():
    ReactionForm = request.get_json()
    Reaction = ReactionService.createReaction(
        mabaidang = ReactionForm['mabaidang'],
        manguoidung = ReactionForm['manguoidung']
    )
    if Reaction is None:
        return "Create Reaction Fail",500
    return "Create Reaction Success", 201
    
@app.route('/get-count-reaction-by-post-id/<int:post_id>',methods=['GET'])    
def getCountReactionByPostId(post_id):
    count = ReactionService.getCountByPostId(mabaidang = post_id)
    return {
        'count': count
    }
    
@app.route('/get-all-reaction-by-post-id/<int:post_id>',methods=['GET'])
def getAllReactionByPostId(post_id):
    Reactions = ReactionService.getAllReactionByPostId(mabaidang = post_id)
    list = []
    for Reaction in Reactions:
        list.append(Reaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/get-all-reaction-by-client-id/<int:client_id>',methods=['GET'])
def getAllReactionById(client_id):
    Reactions = ReactionService.getAllReactionById(manguoidung = client_id)
    list = []
    for Reaction in Reactions:
        list.append(Reaction.serialize())
    return json.dumps(list,indent=4)
    
@app.route('/reaction-find-by-id/<int:client_reaction_id>',methods=['GET'])
def findReactionById(client_reaction_id):
    return jsonify(ReactionService.findReactionById(id=client_reaction_id))

@app.route('/reaction/<int:client_reaction_id>', methods=['DELETE'])
def deleteReaction(client_reaction_id):
    ReactionService.deleteReaction(id = client_reaction_id)
    return "Delete Reaction Success", 201

@app.route('/reaction-delete',methods=['POST'])
def deleteReactionByClientIdAndPostId():
    ReactionJson = request.get_json()
    ReactionService.deleteReactionByClientIdAndPostId(clientId = ReactionJson['clientId'],postId = ReactionJson['postId'])
    return 'Delete Reaction Success',201

# ===================================================================================================== #
# Friend:
@app.route('/friend',methods=['POST'])
def createFriend():
    FriendForm = request.get_json()
    Friend = FriendService.createFriend(manguoidung1 = FriendForm['manguoidung1'],manguoidung2=FriendForm['manguoidung2'])
    if Friend is None:
        return "Create Friend Fail",500
    return "Create Friend Success", 201

@app.route('/find-friend-by-client-id',methods=['POST'])
def findFriendByClientId():
    FriendForm = request.get_json()
    Friend = FriendService.FindFriendByClientId(client1 = FriendForm['client1'],client2=FriendForm['client2'])
    return jsonify(Friend.serialize())

@app.route('/friend-find-by-id/<int:friend_id>',methods=['GET'])
def findFriendById(friend_id):
    return jsonify(FriendService.findFriendById(id = friend_id).serialize())

@app.route('/friend/delete?id1=<int:client_id1>&id2=<int:client_id2>', methods=['DELETE'])
def deleteFriend(client_id1,client_id2):
    FriendService.deleteFriend(client1 = client_id1, client2 = client_id2)
    return "Delete Friend Success", 201

@app.route('/friend-delete',methods=['POST'])
def deleteFriendByClientId():
    FriendForm = request.get_json()
    FriendService.deleteFriend(client1 = FriendForm['client1'],client2 = FriendForm['client2'])
    return 'Delete Friend Success',201

@app.route('/get-all-friend-by-client-id/<int:client_id>',methods=['GET'])
def getAllFriendByClientId(client_id):
    list = main.GetFriendByClientId(client_id)
    return json.dumps(list,indent=4)

@app.route('/get-all-friend-by-friend-request/<int:client_id>',methods=['GET'])
def getAllFriendByFriendRequest(client_id):
    list = main.GetFriendByFriendRequest(client_id)
    return json.dumps(list,indent=4)

@app.route('/get-all-friend-by-friend-response/<int:client_id>',methods=['GET'])
def getAllFriendByFriendResponse(client_id):
    list = main.GetFriendByFriendResponse(client_id)
    return json.dumps(list,indent=4)

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
    datetime_object = datetime.strptime(ClientForm['ngaysinh'],'%Y-%m-%d')
    Client = ClientService.createClient(
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
    datetime_object = datetime.strptime(ClientForm['ngaysinh'],'%Y-%m-%d')
    Client = ClientService.updateClient(hoten = ClientForm['hoten'],
                                        clientId= ClientForm['clientId'],
                                        sdt = ClientForm['sdt'],
                                        email = ClientForm['email'],
                                        gioitinh=True if ClientForm['gioitinh'] == 'true' else False,
                                        ngaysinh = datetime_object)
    if Client is None:
        return "Update client fail", 500
    return "Update client Success", 201

@app.route('/client-password', methods =['POST'])
def updatePassword():
    ClientForm = request.get_json()
    Client = ClientService.updatePassword(clientId = ClientForm['clientId'],matkhaucu = ClientForm['matkhaucu'],matkhaumoi = ClientForm['matkhaumoi'])
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
        
    Client = ClientService.updateAvatar(clientId = ClientForm['clientId'],avt=Avt.filename)
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
        
    Client = ClientService.updateBackgroundImage(clientId = ClientForm['clientId'],backgroundImg=Img.filename)
    if Client is None:
        return "Update background image client fail", 500
    return "Update background image client Success", 201

@app.route('/find-client/<int:client_id>',methods=['GET'])
def findClientById(client_id):
    return jsonify(ClientService.findClientById(id = client_id).serialize())

@app.route('/client-search',methods=['POST'])
def searchClientByKey():
    key = request.get_json()
    Clients = ClientService.searchClient(key = key['key'],clientId=key['clientId'])
    list = []
    for client in Clients:
        list.append(client.serialize())
    return json.dumps(list,indent=4)

@app.route('/client/<int:client_id>', methods=['DELETE'])
def deleteClient(client_id):
    ClientService.deleteClient(id = client_id)
    return "Delete client Success", 200

@app.route('/client/login', methods = ['POST'])
def clientLogin():
    loginInfo = request.get_json()
    Client = ClientService.checkLoginClient(taikhoan = loginInfo['taikhoan'],matkhau= loginInfo['matkhau'])
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
    GroupBackgroundImg = request.files['backgroundImage']

    if GroupBackgroundImg.filename is None:
        flash('No Background Image uploaded')
    elif GroupBackgroundImg and allowed_file(GroupBackgroundImg.filename):
        filenameBackgroundImg = secure_filename(GroupBackgroundImg.filename)
        pathBackgroundImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameBackgroundImg)
        GroupBackgroundImg.save(pathBackgroundImg)
    
    Group = GroupService.createGroup(tennhom = GroupForm['tennhom'],
                                   anhbia=GroupBackgroundImg.filename,
                                   riengtu=True if GroupForm['riengtu'] == 'true' else False)
    
    GroupMember = GroupMemberService.createGroupMember(manhom = Group.GroupId,manguoidung = GroupForm['maquantrivien'],isAdmin=True)
    
    if Group is None:
        return 'Create Group Fail',500
    return 'Create Group Success',201

@app.route("/group-update", methods = ["POST"])
def updateGroup():
    GroupForm = request.get_json()
    Group = GroupService.updateGroup(manhom = GroupForm['manhom'], tennhom = GroupForm['tennhom'],riengtu = GroupForm['riengtu'])
    if Group is None:
        return "Update group fail", 500
    return "Update group Success", 201

@app.route("/group-update-backgroundImg", methods = ["POST"])
def updateBackgroundImageGroup():
    GroupForm = request.form
    Img = request.files['backgroundImg']
    if Img.filename is None:
        flash('No background image uploaded')
    elif Img and allowed_file(Img.filename):
        ImgFilename = secure_filename(Img.filename)
        ImgPath = os.path.join(app.config['UPLOAD_FOLDER'],ImgFilename)
        Img.save(ImgPath)
        
    Group = GroupService.updateBackgroundImage(manhom=GroupForm['manhom'],backgroundImg=Img.filename)
    if Group is None:
        return "Update background image group fail", 500
    return "Update background image group Success", 201

@app.route('/group-find/<int:group_id>',methods=['GET'])
def findGroupById(group_id):
    return jsonify(GroupService.findGroupById(id = group_id).serialize())

@app.route('/group-search',methods=['POST'])
def searchGroupByKey():
    key = request.get_json()
    Groups = GroupService.searchGroup(key = key['key'])
    list = []
    for group in Groups:
        list.append(group.serialize())
    return json.dumps(list,indent=4)

@app.route('/group/<int:group_id>', methods=['DELETE'])
def deleteGroup(group_id):
    GroupService.deleteGroup(id=group_id)
    return "Delete group Success", 200

@app.route('/get-all-group-by-client-id/<int:client_id>',methods=['GET'])
def getAllGroupByClientId(client_id):
    list = main.GetAllGroupByClientId(clientId = client_id)
    return json.dumps(list,indent=4)

@app.route('/get-all-group-by-group-request/<int:client_id>',methods=['GET'])
def getAllGroupByGroupRequest(client_id):
    list = main.GetAllGroupByGroupRequest(clientId = client_id)
    return json.dumps(list,indent=4)
    

# ===================================================================================================== #
# Thành viên nhóm:
@app.route('/group-member',methods=['POST'])
def createGroupMember():
    GroupMemberForm = request.get_json()
    GroupMember = GroupMemberService.createGroupMember(manhom = GroupMemberForm['manhom'],manguoidung= GroupMemberForm['manguoidung'],isAdmin = GroupMemberForm['isAdmin'])
    if GroupMember is None:
        return "Create Group Member Fail",500
    return "Create Group Member Success", 201

@app.route('/group-member-update',methods=['POST'])
def updateGroupMember():
    GroupMemberForm = request.get_json()
    GroupMember = GroupMemberService.updateGroupMember(manhom = GroupMemberForm['manhom'],manguoidung=GroupMemberForm['manguoidung'],isAdmin=GroupMemberForm['isAdmin'])
    if GroupMember is None:
        return 'Update Group Member Fail',500
    return 'Update Group Member Success',201

@app.route('/get-all-group-member-by-group-id/<int:group_id>',methods=['GET'])
def getAllGroupMemberByGroupId(group_id):
    GroupMembers = GroupMemberService.getAllGroupMemberByGroupId(manhom = group_id)
    list = []
    for GroupMember in GroupMembers:
        list.append(GroupMember.serialize())
    return json.dumps(list,indent=4)

@app.route('/group-member-find-by-id/<int:group_member_id>',methods=['GET'])
def findGroupMemberById(group_member_id):
    return jsonify(GroupMemberService.findGroupMemberById(id=group_member_id).serialize())

@app.route('/find-group-member-by-client-id',methods=['POST'])
def findGroupMemberByClientId():
    GroupMemberJson = request.get_json()
    return jsonify(GroupMemberService.findGroupMemberByClientIdAndGroupId(clientId=GroupMemberJson['clientId'],groupId=GroupMemberJson['groupId']).serialize())
    
@app.route('/group-member-get-all-by-client-id/<int:client_id>',methods=['GET'])
def getAllGroupMemberByClientId(client_id):
    GroupMembers = GroupMemberService.getAllGroupMemberByClientId(manguoidung = client_id)
    list = []
    for GroupMember in GroupMembers:
        list.append(GroupMember.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-member-from-group-member/<int:group_id>',methods=['GET'])
def getAllClientFromGroupMember(group_id):
    list = main.GetAllClientFromGroupMember(group_id)
    return json.dumps(list,indent=4)

@app.route('/group-member/delete', methods=['POST'])
def deleteGroupMemberByClientIdAndGroupId():
    GroupMemberJson = request.get_json()
    GroupMemberService.deleteGroupMemberByClientIdAndGroupId(clientId = GroupMemberJson['clientId'],groupId = GroupMemberJson['groupId'])
    return "Delete Group Member Success", 201

@app.route('/group-member/<int:group_member_id>', methods=['DELETE'])
def deleteGroupMember(group_member_id):
    GroupMemberService.deleteGroupMember(id = group_member_id)
    return "Delete Group Member Success", 201



@app.route('/group-member-delete-and-update-new-admin',methods=['POST'])
def deleteGroupMemberAndUpdateNewAdmin():
    GroupMemberJson = request.get_json()
    GroupMemberService.deleteGroupMemberAndUpdateNewAdmin(clientId=GroupMemberJson['clientId'],groupId=GroupMemberJson['groupId'],adminId=GroupMemberJson['adminId'])
    return 'Delete Group Member Success',201
# ===================================================================================================== #
# Tin nhắn:
@app.route('/message',methods=['POST'])
def createMessage():
    MessageForm = request.get_json()
    Message = MessageService.createTinNhan(
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
    Messages = MessageService.getAllMessageByClientId(nguoidung1 = MessageForm['nguoidung1'],nguoidung2 = MessageForm['nguoidung2'])
    list = []
    for Message in Messages:
        list.append(Message.serialize())
    return json.dumps(list,indent=4)

@app.route('/message-find-by-id/<int:message_id>',methods=['GET'])
def findMessageById(message_id):
    return jsonify(MessageService.findMessageById(id=message_id).serialize())

@app.route('/message/<int:message_id>', methods=['DELETE'])
def deleteMessage(message_id):
    MessageService.deleteMessage(id = message_id)
    return "Delete Message Success", 201



# ===================================================================================================== #
# Xét duyệt bài đăng nhóm:
@app.route('/post-confirm',methods=['POST'])
def createPostConfirm():
    PostConfirmForm = request.form()
    Img = request.files['image']
    check = False
    if Img and allowed_file(Img.filename):
        filenameImg = secure_filename(Img.filename)
        pathImg = os.path.join(app.config['UPLOAD_FOLDER'],filenameImg)
        Img.save(pathImg)
        check = True
        
    PostConfirm = PostConfirmService.createPostConfirm(
        manhom = PostConfirmForm['manhom'],
        manguoidung = PostConfirmForm['manguoidung'],
        noidung = PostConfirmForm['noidung'],
        anh = None if check == False else Img.filename
    )
    if PostConfirm is None:
        return "Create Confirm Post Fail",500
    return "Create Confirm Post Success", 201

@app.route('/get-all-post-confirm-by-group-id/<int:group_id>',methods=['GET'])
def getAllPostConfirmByGroupId(group_id):
    PostConfirms = PostConfirmService.getAllPostConfirmByGroupId(manhom = group_id)
    list = []
    for PostConfirm in PostConfirms:
        list.append(PostConfirm.serialize())
    return json.dumps(list,indent=4)

@app.route('/post-confirm-find-by-id/<int:confirm_post_id>',methods=['GET'])
def findPostConfirmById(confirm_post_id):
    return jsonify(PostConfirmService.findPostConfirmById(id = confirm_post_id).serialize())

@app.route('/post-confirm/<int:confirm_post_id>', methods=['DELETE'])
def deletePostConfirm(confirm_post_id):
    PostConfirmService.deletePostConfirm(id = confirm_post_id)
    return "Delete Confirm Post Success", 201

@app.route('/post-confirmed/<int:confirm_post_id>',methods=['POST'])
def confirmedPost(confirm_post_id):
    PostConfirm = PostConfirmService.confirmed(id = confirm_post_id)
    if PostConfirm is None:
        return 'Confirm Post Fail',500
    else:
        return 'Confirm Post Success',201
    

# ===================================================================================================== #
# Yêu cầu kết bạn:
@app.route('/friend-request',methods=['POST'])
def createFriendRequest():
    FriendRequestForm = request.get_json()
    FriendRequest = FriendRequestService.createFriendRequest(nguoinhan = FriendRequestForm['nguoinhan'],nguoigui = FriendRequestForm['nguoigui'])
    if FriendRequest is None:
        return "Create Friend Request Fail",500
    return "Create Friend Request Success", 201

@app.route('/get-all-friend-request-by-receiver/<int:receiver_id>',methods=['GET'])
def getAllFriendRequestByReceiver(receiver_id):
    FriendRequests = FriendRequestService.getAllFriendRequestByReceiverId(manguoinhan = receiver_id)
    list = []
    for FriendRequest in FriendRequests:
        list.append(FriendRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-friend-request-by-sender/<int:sender_id>',methods=['GET'])
def getAllFriendRequestBySender(sender_id):
    FriendRequests = FriendRequestService.getAllFriendRequestBySenderId(manguoinhan = sender_id)
    list = []
    for FriendRequest in FriendRequests:
        list.append(FriendRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/friend-request-find-by-id/<int:friend_request_id>',methods=['GET'])
def findFriendRequestById(friend_request_id):
    return jsonify(FriendRequestService.findFriendRequestById(id = friend_request_id).serialize())

@app.route('/find-friend-request-by-client-id',methods=['POST'])
def findFriendRequestByClientId():
    FriendRequestJson = request.get_json()
    return jsonify(FriendRequestService.findFriendRequestByClientId(client1=FriendRequestJson['client1'],client2=FriendRequestJson['client2']).serialize())

@app.route('/friend-request/<int:friend_request_id>',methods=['DELETE'])
def deleteFriendRequest(friend_request_id):
    FriendRequestService.deleteFriendRequest(id = friend_request_id)
    return "Delete Friend Request Success", 201

@app.route('/friend-request-delete',methods=['POST'])
def deleteFriendRequestByClientId():
    ClientId = request.get_json()
    FriendRequestService.deleteFriendRequestByClientId(receiverId=ClientId['receiverId'],senderId=ClientId['senderId'])
    return 'Delete Friend Request Success',201

@app.route('/friend-request-confirm',methods=['POST'])
def confirmFriendRequest():
    ClientId = request.get_json()
    FriendRequestService.confirmFriendRequest(receiverId = ClientId['receiverId'],senderId=ClientId['senderId'])
    return 'Confirm Friend Request Success',201
# ===================================================================================================== #
# Yêu cầu tham gia nhóm: 
@app.route('/group-request',methods=['POST'])
def createGroupRequest():
    GroupRequestForm = request.get_json()
    GroupRequest = GroupRequestService.createGroupRequest(manhom = GroupRequestForm['manhom'],manguoidung = GroupRequestForm['manguoidung'])
    if GroupRequest is None:
        return "Create Group Request Fail",500
    return "Create Group Request Success", 201

@app.route('/get-all-group-request-by-client-id/<int:client_id>',methods=['GET'])
def getAllGroupRequestByReceiver(client_id):
    GroupRequests = GroupRequestService.getAllGroupRequestByClientId(manguoidung = client_id)
    list = []
    for GroupRequest in GroupRequests:
        list.append(GroupRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-group-request-by-group-id/<int:group_id>',methods=['GET'])
def getAllGroupRequestByGroupId(group_id):
    GroupRequests = GroupRequestService.getAllGroupRequestByGroupId(manhom = group_id)
    list = []
    for GroupRequest in GroupRequests:
        list.append(GroupRequest.serialize())
    return json.dumps(list,indent=4)

@app.route('/get-all-member-from-group-request/<int:group_id>',methods=['GET'])
def getAllMemberFromGroupRequest(group_id):
    list = main.GetAllMemberFromGroupRequest(groupId= group_id)
    return json.dumps(list,indent=4)

@app.route('/group-request-find-by-id/<int:group_request_id>',methods=['GET'])
def findGroupRequestById(group_request_id):
    return jsonify(GroupRequestService.findGroupRequestById(id = group_request_id).serialize())

@app.route('/find-group-request-by-client-id',methods=['POST'])
def findGroupRequestByClientId():
    GroupRequestJson = request.get_json()
    return jsonify(GroupRequestService.findGroupRequestByClientIdAndGroupId(clientId = GroupRequestJson['clientId'],groupId=GroupRequestJson['groupId']).serialize())

@app.route('/group-request-delete/<int:group_request_id>',methods=['DELETE'])
def deleteGroupRequest(group_request_id):
    GroupRequestService.deleteGroupRequest(id = group_request_id)
    return "Delete Group Request Success", 201

@app.route('/group-request-delete',methods=['POST'])
def deleteGroupRequestByClientIdAndGroupId():
    GroupRequestForm = request.get_json()
    GroupRequestService.deleteByClientIdAndGroupId(clientId = GroupRequestForm['clientId'],groupId = GroupRequestForm['groupId'])
    return 'Delete Group Request Success',201

@app.route('/group-request-confirm',methods=['POST'])
def confirmGroupRequest():
    GroupRequestJson = request.get_json()
    GroupRequestService.confirmGroupRequestByClientIdAdnGroupId(clientId=GroupRequestJson['clientId'],groupId=GroupRequestJson['groupId'])
    return 'Confirm Success'