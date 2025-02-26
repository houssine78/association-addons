/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { Dialog } from "@web/core/dialog/dialog";
import { useService } from "@web/core/utils/hooks";
import { useRef, Component } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

export class UrlDialog extends Component {
    setup() {
        this.title = _t("Add Attachment From URL");
        this.notification = useService("notification");
        this.urlRef = useRef("url"); 
    }

    close() {
        this.props.close && this.props.close();
    }
    async onClickConfirm(){
        var self = this;
        var urlInput = this.urlRef.el;
        if (urlInput && urlInput.value){
            const is_validUrl = this.validURL(urlInput.value);
            if (is_validUrl){
                const data = await rpc("/upload_attachment_form_url/get_base64_attachment_data", {
                    url : urlInput.value,
                });
                if (data.base64,data.file_name,data.mime_type){
                    await self.props.uploadUrlImage(data);
                    self.props.close();
                }else{
                    this.notification.add(_t("Please upload a valid URL."));
                }
            }else{
                this.notification.add(_t("Please enter a valid URL."));
            }
        }
        else{
            this.notification.add(_t("Please enter a URL."));
        }
        
    }

    validURL(str) {
        var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
          '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
          '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
          '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
        return !!pattern.test(str);
    }
}
UrlDialog.components = { Dialog };
UrlDialog.template = "upload_attachment_form_url.UrlDialog";
UrlDialog.defaultProps = {

};
