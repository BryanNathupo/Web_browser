import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtWebEngine 1.10

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Webrowser")

    Rectangle {
        id: url_search
        width: parent.width
        height: parent.height
        color: "grey"
        ColumnLayout{
            spacing: 10
            anchors.fill: parent
            //The row below holds a textfield and search Button
            RowLayout {
                id: rowlayout
                spacing: 10

                //anchors.centerIn: parent

                Item {
                    Layout.preferredWidth: 280
                }
                Rectangle {
                    id: previousRect
                    color: "grey"
                    width: 50
                    height: 40
                    Text{
                        anchors.centerIn: parent
                        id: previus
                        text: "<"
                        font.pointSize: 30
                        color: "blue"
                        //Navigating between the pages

                    }
                    MouseArea{
                        id: backMousearea
                        anchors.fill: previousRect
                        hoverEnabled: true
                        onClicked: {
                            myWebView.goBack()
                            console.log("Im clicked")
                        }

                    }
                }

                TextField {
                    id: urlTextField
                    placeholderText: "Enter url here..."
                    Layout.preferredWidth: 600
                    background: Rectangle {
                        radius: 10
                    }

                }

                Button {
                    id: search
                    text: qsTr("Search")
                    implicitWidth: 200
                    background: Rectangle {
                        radius: 10
                    }
                    onClicked: {
                         myWebView.url = urlTextField.text
                    }

                }
                Rectangle {
                    id: nextRect
                    color: "grey"
                    width: 50
                    height: 40
                    Text{
                        id: next
                        anchors.centerIn: parent
                        text: ">"
                        font.pointSize: 30
                        color: "blue"
                        //Navigating between the pages

                    }
                    MouseArea{
                        anchors.fill: nextRect
                        onClicked: {
                            myWebView.goForward()
                            console.log("Forward is Clicked!")
                        }
                    }
                }


            }

            Rectangle {
                id: webViewRectangle
                Layout.fillHeight: true
                Layout.fillWidth: true
                color: "white"

                WebEngineView{
                    id: myWebView
                    anchors.fill: parent
                    //Removing the static url
                    url: " "
                }

            }

        }

    }

}
