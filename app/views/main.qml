import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 1280
    height: 960
    visible: true
    title: "Gestion de stock"
    visibility: Window.Maximized

    ColumnLayout{
        RowLayout{
            Image {
                source: "../images/odoo_inventory_app.png"
                width:40
                height:40
                sourceSize.width:40
                sourceSize.height:40
                fillMode: Image.PreserveAspectFit
                clip: true
            }

            MenuBar{
                background: Rectangle{
                    color: "#FFFFFF"
                }
                Menu{
                    title:"Operation"
                    MenuItem{
                        text:"Transfert"
                        onTriggered: pageLoader.source = "operation_transfert.qml"
                    }
                    MenuItem{
                        text:"Replenishment"
                        onTriggered: pageLoader.source = "operation_replenishment.qml"
                    }
                }
                Menu{
                    title:"Product"
                    MenuItem{
                        text:"Product"
                        onTriggered: pageLoader.source = "product_product.qml"
                    }
                    MenuItem{
                        text:"Product variant"
                        onTriggered: pageLoader.source = "product_product_variant.qml"
                    }
                }
                Menu{
                    title:"Reporting"
                    MenuItem{
                        text:"Stock"
                        onTriggered: pageLoader.source = "reporting_stock.qml"
                    }
                    MenuItem{
                        text:"Location"
                        onTriggered: pageLoader.source = "reporting_location.qml"
                    }
                }
                Menu{
                    title:"Configuration"
                    MenuItem{
                        text:"Vendor"
                        onTriggered: pageLoader.source = "configuration_vendor.qml"
                    }
                    MenuItem{
                        text:"Location"
                        onTriggered: pageLoader.source = "configuration_location.qml"
                    }
                }
            }
        }
        Loader { id: pageLoader }
    }

    

}