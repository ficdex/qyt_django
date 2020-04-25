from django import forms
from qyt_device.models import Devicetype, Devicedb


class AddDeviceForm(forms.Form):
    # 为了添加必选项前面的星号
    # 下面是模板内的内容
    """
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color: red;
    }
    < / style >
    """
    required_css_class = 'required'  # 这是Form.required_css_class属性, use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for="id_name">设备名称:</label>
    # 不添加效果如下
    # <label for="id_name">设备名称:</label>

    # 设备名称,最小长度2,最大长度50,
    # label后面填写的内容,在表单中显示为名字,
    # 必选(required=True其实是默认值)
    # attrs={"class": "form-control"} 主要作用是style it in Bootstrap
    name = forms.CharField(max_length=50,
                           min_length=2,
                           label='设备名称',
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    # IP地址
    ip = forms.GenericIPAddressField(label='IP地址',
                                     required=True,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    # 设备描述信息
    description = forms.CharField(label='描述',
                                  required=False,
                                  widget=forms.Textarea(attrs={"class": "form-control"}))
    # SNMP只读Community
    snmp_ro_community = forms.CharField(label='SNMP只读Community',
                                        required=True,
                                        widget=forms.TextInput(attrs={"class": "form-control"}))

    # SNMP读写Community
    snmp_rw_community = forms.CharField(label='SNMP读写Community',
                                        required=False,
                                        widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH用户名
    ssh_username = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='SSH用户名',
                                   required=False,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    # SSH密码
    ssh_password = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='SSH密码',
                                   required=False,
                                   widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # enable密码
    enable_password = forms.CharField(max_length=50,
                                      min_length=2,
                                      label='Enable密码',
                                      required=False,
                                      widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # 设备类型
    type_choices = [(dt.id, dt.name) for dt in Devicetype.objects.all()]
    type = forms.CharField(max_length=10,
                           label='设备类型',
                           widget=forms.Select(choices=type_choices, attrs={"class": "form-control"}))

    def clean_ip_address(self):  # 对IP地址的唯一性进行校验,注意格式为clean+校验变量
        ip_address = self.cleaned_data['ip']  # 提取客户输入的电话号码
        # 在数据库中查找是否存在这个IP地址
        existing = Devicedb.objects.filter(ip=ip_address).exists()
        # 如果存在就显示校验错误信息
        if existing:
            raise forms.ValidationError("IP地址已经存在")
        # 如果校验成功就返回IP地址
        return ip_address

    def clean_password(self):
        password = self.cleaned_data['ssh_password']
        username = self.cleaned_data['ssh_username']
        if not (password and username):
            raise forms.ValidationError("用户名和密码需要同时填写")
        return password