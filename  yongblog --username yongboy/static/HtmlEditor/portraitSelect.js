// img attr: name, alt, shortcut
var imagePath = "http://mimg.163.com/popo/";
var imageWidth = 19;
var imageHeight = 19;
var countPerRow = 14;
var sHTML = "";
var sHTMLHead = "";
function portrait(name, alt, shortcut)
{
    this.name = name;
    this.alt = alt;
    this.shortcut = shortcut;
}

    var imgArray = new Array();
    imgArray[0] = new portrait("smile01.gif", "΢Ц", ":)");
    imgArray[1] = new portrait("smile02.gif", "����Ц", ":))");
    imgArray[2] = new portrait("smile03.gif", "գ��" ,"");
    imgArray[3] = new portrait("smile04.gif", "����" ,"");
    imgArray[4] = new portrait("smile05.gif", "����Ц��" ,"");
    imgArray[5] = new portrait("smile06.gif", "�����Ц" ,"");
    imgArray[6] = new portrait("smile07.gif", "����" ,"");
    imgArray[7] = new portrait("smile08.gif", "����" ,"");
    imgArray[8] = new portrait("smile09.gif", "����" ,"");
    imgArray[9] = new portrait("smile10.gif", "�ѹ�" ,"");
    imgArray[10] = new portrait("smile11.gif", "����" , "");
    imgArray[11] = new portrait("smile12.gif", "ʧ��" , "");
    imgArray[12] = new portrait("smile13.gif", "����" , "");
    imgArray[13] = new portrait("smile14.gif", "�ú�Ц" , "");
    imgArray[14] = new portrait("smile15.gif", "�" , "");
    imgArray[15] = new portrait("smile16.gif", "�絽��" , "");
    imgArray[16] = new portrait("smile17.gif", "��" , "");
    imgArray[17] = new portrait("smile18.gif", "����ˮ��" , "");
    imgArray[18] = new portrait("smile19.gif", "������" , "");
    imgArray[19] = new portrait("smile20.gif", "����" , "");
    imgArray[20] = new portrait("smile21.gif", "������" , "");
    imgArray[21] = new portrait("smile22.gif", "��" , "");
    imgArray[22] = new portrait("smile23.gif", "������" , "");
    imgArray[23] = new portrait("smile24.gif", "��˵" , "");
    imgArray[24] = new portrait("smile25.gif", "��" , "");
    imgArray[25] = new portrait("smile26.gif", "ɫ����" , "");
    imgArray[26] = new portrait("smile27.gif", "��ѵ" , "");
    imgArray[27] = new portrait("smile28.gif", "�ɰ�" , "");
    imgArray[28] = new portrait("smile29.gif", "YEAH" , "");
    imgArray[29] = new portrait("smile30.gif", "����" , "");
    imgArray[30] = new portrait("smile31.gif", "����" , "");
    imgArray[31] = new portrait("smile32.gif", "����" , "");
    imgArray[32] = new portrait("smile33.gif", "��Ľ��" , "");
    imgArray[33] = new portrait("smile34.gif", "��" , "");
    imgArray[34] = new portrait("smile35.gif", "�ڱǿ�" , "");
    imgArray[35] = new portrait("smile36.gif", "����" , "");
    imgArray[36] = new portrait("smile37.gif", "����" , "");
    imgArray[37] = new portrait("smile38.gif", "����" , "");
    imgArray[38] = new portrait("smile39.gif", "�ϴ�" , "");
    imgArray[39] = new portrait("smile40.gif", "Ƿ��" , "");
    imgArray[40] = new portrait("smile41.gif", "����" , "");
    imgArray[41] = new portrait("smile42.gif", "����æ" , "");
    imgArray[42] = new portrait("smile43.gif", "���" , "");
    imgArray[43] = new portrait("smile44.gif", "͵͵Ц" , "");
    imgArray[44] = new portrait("smile45.gif", "�ͻ�����" , "");
    imgArray[45] = new portrait("smile46.gif", "������һ��" , "");
    imgArray[46] = new portrait("smile47.gif", "������" , "");
    imgArray[47] = new portrait("smile48.gif", "�ݰ�" , "");
    imgArray[48] = new portrait("49.gif", "��������" , "");
    imgArray[49] = new portrait("50.gif", "����Ů��" , "");
    imgArray[50] = new portrait("51.gif", "õ��" , "");
    imgArray[51] = new portrait("52.gif", "�ð���" , "");
    imgArray[52] = new portrait("53.gif", "������" , "");
    imgArray[53] = new portrait("54.gif", "����" , "");
    imgArray[54] = new portrait("55.gif", "NO" , "");
    imgArray[55] = new portrait("56.gif", "YES" , "");
	imgArray[56] = new portrait("57.gif", "�ո���" , "");
	imgArray[57] = new portrait("58.gif", "������" , "");
	imgArray[58] = new portrait("59.gif", "����" , "");
	imgArray[59] = new portrait("60.gif", "CALL��" , "");
	imgArray[60] = new portrait("61.gif", "��Ѫ�ĵ�" , "");
	imgArray[61] = new portrait("62.gif", "ը��" , "");
	imgArray[62] = new portrait("63.gif", "����" , "");
	imgArray[63] = new portrait("64.gif", "������" , "");
	imgArray[64] = new portrait("65.gif", "��Ѫ����" , "");
	imgArray[65] = new portrait("66.gif", "���" , "");
	imgArray[66] = new portrait("67.gif", "��һ��" , "");
	imgArray[67] = new portrait("68.gif", "����" , "");
	imgArray[68] = new portrait("69.gif", "��绰" , "");
	imgArray[69] = new portrait("70.gif", "��" , "");
	imgArray[70] = new portrait("71.gif", "����" , "");
	imgArray[71] = new portrait("72.gif", "����" , "");
	imgArray[72] = new portrait("73.gif", "��Ǯ" , "");
	imgArray[73] = new portrait("74.gif", "̫��" , "");
	imgArray[74] = new portrait("75.gif", "����" , "");
	imgArray[75] = new portrait("76.gif", "����" , "");
	imgArray[76] = new portrait("77.gif", "Сè" , "");
	imgArray[77] = new portrait("78.gif", "С��" , "");
	imgArray[78] = new portrait("79.gif", "��ͷ" , "");
	imgArray[79] = new portrait("80.gif", "��ˮ" , "");
	imgArray[80] = new portrait("81.gif", "����" , "");
	imgArray[81] = new portrait("82.gif", "����" , "");
	imgArray[82] = new portrait("83.gif", "����" , "");
	imgArray[83] = new portrait("84.gif", "Լ��" , "");


function drawSpace()
{
    sHTML +='</tr><tr align="left" bgcolor="#f8f8f8" class="unnamed1">';
}
function drawPortrat( index )
{
    if (index<0 || index>imgArray.length) return;
    var portratContent ='<img src="' + imagePath + imgArray[index].name + '" ' +
                        'alt="' + imgArray[index].alt + '" ' +
                        'width="' + imageWidth + '" ' + 
                        'height="' + imageHeight + '" >';
    sHTML +='<td align="center">';
    sHTML +=portratContent;
    sHTML +='</td>';
}
function drawPortratsHead()
{
	sHTMLHead = "";
    sHTMLHead +='<td colspan="' + countPerRow + '"  align="center"> <strong>����</strong></td>';
	return sHTMLHead;
}
function drawPortrats()
{
    var i = 0;
	sHTML = "";
    for (i=0; i<imgArray.length; i++) {
        if (i>0 && i%countPerRow==0)    drawSpace();
        drawPortrat( i );
    }
	return sHTML;
}
function MouseClick( index )
{
    window.returnValue = imagePath + imgArray[index].name;
    window.close();
}