from vali_objects.cmw.cmw_objects.cmw_miner import CMWMiner


class CMWStreamType:
    def __init__(self):
        self.stream_type = None
        self.topic_id = None
        self.miners = []

    def set_stream_type(self, stream_type):
        self.stream_type = stream_type
        return self

    def set_topic_id(self, topic_id):
        self.topic_id = topic_id
        return self

    def add_miner(self, miner: CMWMiner):
        self.miners.append(miner)

    def get_miner(self, miner_id):
        for miner in self.miners:
            if miner.miner_id == miner_id:
                return miner
        return None

    # def setup_cmw_stream_type(self, cmw_stream_type):
    #     for miner_uid, miner_values in cmw_stream_type["miners"].items():
    #         self.miners[miner_uid] = CMWMiner(miner_values["wins"], miner_values["o_wins"])
    #     return self

